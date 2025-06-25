import struct
import time
from collections import defaultdict
from datetime import datetime
import stat
import os
import hashlib
import re



class Yaffs2Forensic:
    
    
    class Result:
        def __init__(self, success, data=None, error=None):
            self.success = success
            self.data = data
            self.error = error
        
        def __bool__(self):
            return self.success
        
        def __repr__(self):
            return f"<Result success={self.success} data={self.data} error={self.error}>"
    
    # === Public API ===
    def __init__(self, opt):
        self.image          = opt['image']  if 'image' in opt else None
        if self.image is None:
            raise Exception("image file is missing.")
        self.debug          = opt['debug']  if 'debug' in opt else 0
        try:
            self.handle = open(self.image, "rb")
        except FileNotFoundError:
            raise RuntimeError(f"Image file not found: {self.image}")
        except PermissionError:
            raise RuntimeError(f"No permission to read the image file: {self.image}")
        except OSError as e:
            raise RuntimeError(f"Unable to open image file '{self.image}': {e}")
        
        self.headers                = defaultdict(list)
        self.data_chunks            = defaultdict(list)
        self.objects                = defaultdict(list)
        self.directories_created    = {}
        self.DEFAULT_MODE           = 420
        self.DEFAULT_CTIME          = 1
        self.ROOT_PARENT_ID         = 1     # '/'
        self.YAFFS_MAX_NAME_LENGTH  = 254
        self.YAFFS_MAX_ALIAS_LENGTH = 160
        self.SEQUENCE_NUMBER        = [4096, 4026531584]
        self.PAGESIZE               = 512
        self.OOBSIZE                = 16
        self.ENDIAN                 = "little"
        
        self.ENDIANNESS_OPTIONS  = ["little", "big"]
        self.CANDIDATES = [
            (2048, 64),
            (4096, 128),
            (512, 16),
            (8192, 224),
            (16384, 448),
        ]
        # Object type IDs
        self.OBJECT_TYPE_ID = {
            0: 'YAFFS_OBJECT_TYPE_UNKNOWN',
            1: 'YAFFS_OBJECT_TYPE_FILE',
            2: 'YAFFS_OBJECT_TYPE_SYMLINK',
            3: 'YAFFS_OBJECT_TYPE_DIRECTORY',
            4: 'YAFFS_OBJECT_TYPE_HARDLINK',
            5: 'YAFFS_OBJECT_TYPE_SPECIAL',
        }
        
        self.OBJECT_MODE = {
            0: stat.S_IFREG,
            1: stat.S_IFREG,
            2: stat.S_IFLNK,
            3: stat.S_IFDIR,
            4: stat.S_IFLNK,
            5: stat.S_IFCHR,
            6: stat.S_IFBLK,
            7: stat.S_IFIFO,
            8: stat.S_IFSOCK,
        }
        
        # Special parent IDs
        self.SPECIAL_PARENT_ID = {
            1: 'YAFFS_OBJECTID_ROOT',
            2: 'YAFFS_OBJECTID_LOSTNFOUND',
            3: 'YAFFS_OBJECTID_UNLINKED',
            4: 'YAFFS_OBJECTID_DELETED',
        }
        
        # Fields position/length in OOB part
        self.OOB_LAYOUT = [
            { 'field': 'blockstate',        'pos': (1    , 1) },
            { 'field': 'sequence_number',   'pos': (2    , 4) },
            { 'field': 'object_id',         'pos': (6    , 4) },
            { 'field': 'chunk_id',          'pos': (10   , 4) },
            { 'field': 'n_bytes',           'pos': (14   , 2) },
        ]
        
        # Fields position/length in DATA part
        self.DATA_LAYOUT = [
            { 'field': 'junk0',             'pos': (0                                                               , 10                            ) },      
            { 'field': 'name',              'pos': (10                                                              , self.YAFFS_MAX_NAME_LENGTH    ) },      # File name
            { 'field': 'junk1',             'pos': (self.YAFFS_MAX_NAME_LENGTH + 10                                 , 4                             ) },      # Should be 0xFFFFFFFF
            { 'field': 'yst_mode',          'pos': (self.YAFFS_MAX_NAME_LENGTH + 14                                 , 4                             ) },      # File mode and ownership info
            { 'field': 'yst_uid',           'pos': (self.YAFFS_MAX_NAME_LENGTH + 18                                 , 4                             ) },      
            { 'field': 'yst_gid',           'pos': (self.YAFFS_MAX_NAME_LENGTH + 22                                 , 4                             ) },      
            { 'field': 'yst_atime',         'pos': (self.YAFFS_MAX_NAME_LENGTH + 26                                 , 4                             ) },      # File timestamp info
            { 'field': 'yst_mtime',         'pos': (self.YAFFS_MAX_NAME_LENGTH + 30                                 , 4                             ) },      
            { 'field': 'yst_ctime',         'pos': (self.YAFFS_MAX_NAME_LENGTH + 34                                 , 4                             ) },      
            { 'field': 'file_size_low',     'pos': (self.YAFFS_MAX_NAME_LENGTH + 38                                 , 4                             ) },      # <<< Low 32 bits of file size
            { 'field': 'equiv_id',          'pos': (self.YAFFS_MAX_NAME_LENGTH + 42                                 , 4                             ) },      # Used for hard links, specifies the object ID of the file to be hardlinked to.
            { 'field': 'alias',             'pos': (self.YAFFS_MAX_NAME_LENGTH + 46                                 , self.YAFFS_MAX_ALIAS_LENGTH   ) },      # Aliases are for symlinks only
            { 'field': 'yst_rdev',          'pos': (self.YAFFS_MAX_NAME_LENGTH + self.YAFFS_MAX_ALIAS_LENGTH + 46   , 4                             ) },      # Stuff for block and char devices (equivalent of stat.st_rdev in C)
            { 'field': 'win_ctime_1',       'pos': (self.YAFFS_MAX_NAME_LENGTH + self.YAFFS_MAX_ALIAS_LENGTH + 50   , 4                             ) },      # Appears to be for timestamp stuff for WinCE
            { 'field': 'win_ctime_2',       'pos': (self.YAFFS_MAX_NAME_LENGTH + self.YAFFS_MAX_ALIAS_LENGTH + 54   , 4                             ) },      
            { 'field': 'win_atime_1',       'pos': (self.YAFFS_MAX_NAME_LENGTH + self.YAFFS_MAX_ALIAS_LENGTH + 58   , 4                             ) },      
            { 'field': 'win_atime_2',       'pos': (self.YAFFS_MAX_NAME_LENGTH + self.YAFFS_MAX_ALIAS_LENGTH + 62   , 4                             ) },      
            { 'field': 'win_mtime_1',       'pos': (self.YAFFS_MAX_NAME_LENGTH + self.YAFFS_MAX_ALIAS_LENGTH + 66   , 4                             ) },      
            { 'field': 'win_mtime_2',       'pos': (self.YAFFS_MAX_NAME_LENGTH + self.YAFFS_MAX_ALIAS_LENGTH + 70   , 4                             ) },      
                  
            { 'field': 'inband_shad_obj_id','pos': (self.YAFFS_MAX_NAME_LENGTH + self.YAFFS_MAX_ALIAS_LENGTH + 74   , 4                             ) },      # The only thing this code uses from these entries is file_size_high (high 32 bits of the file size).
            { 'field': 'inband_is_shrink',  'pos': (self.YAFFS_MAX_NAME_LENGTH + self.YAFFS_MAX_ALIAS_LENGTH + 78   , 4                             ) },      
            { 'field': 'file_size_high',    'pos': (self.YAFFS_MAX_NAME_LENGTH + self.YAFFS_MAX_ALIAS_LENGTH + 82   , 4                             ) },      # <<< High 32 bits of file_size
            { 'field': 'reserved',          'pos': (self.YAFFS_MAX_NAME_LENGTH + self.YAFFS_MAX_ALIAS_LENGTH + 86   , 1                             ) },      
            { 'field': 'shadows_obj',       'pos': (self.YAFFS_MAX_NAME_LENGTH + self.YAFFS_MAX_ALIAS_LENGTH + 87   , 4                             ) },      
            { 'field': 'is_shrink',         'pos': (self.YAFFS_MAX_NAME_LENGTH + self.YAFFS_MAX_ALIAS_LENGTH + 91   , 4                             ) },      
        ]
    
    
    def set_params (self, opt):         # ← config
        """
        Sets internal parameters for page size, OOB size, and endianness.
        
        Args:
            opt (dict): Optional dictionary with any of the following keys:
                - 'pagesize' (int): Size of data pages.
                - 'oobsize' (int): Size of OOB area.
                - 'endianness' (str): Byte order ('little' or 'big').
        
        Notes:
            If a parameter is not provided, a default value is used.
        """
        self.pagesize   = opt['pagesize']   if 'pagesize'   in opt else self.PAGESIZE
        self.oobsize    = opt['oobsize']    if 'oobsize'    in opt else self.OOBSIZE
        self.endianness = opt['endianness'] if 'endianness' in opt else self.ENDIAN
        self.total_chunk_size = self.pagesize + self.oobsize
    
    
    def autodetect_format(self):        # ← detection
        """
        Attempts to automatically detect the image format from candidate tuples.
        
        For each (pagesize, oobsize) candidate and each endianness, computes a plausibility score
        by evaluating a number of chunks. Selects the best scoring combination as the most likely format.
        
        Returns:
            list: A 4-element list containing:
                [score (int), pagesize (int), oobsize (int), endianness (str)]
                representing the best detected format.
        """
        results = []
        for pagesize, oobsize in self.CANDIDATES:
            for endianness in self.ENDIANNESS_OPTIONS:
                score = self.__score_format(pagesize=pagesize, oobsize=oobsize, endianness=endianness, max_blocks=1000)
                results.append((score, pagesize, oobsize, endianness))
                self.__log(1, f"    testing format {pagesize}+{oobsize} in {endianness}-endian -> Score : {score}")
    
        results.sort(reverse=True)
        best = results[0]
        self.__log(0, f"==> Best format detected : {best[1]} / {best[2]} in {best[3]}-endian (score {best[0]})")
        return best
    
    
    def list_obj (self, opt):           # ← final user view
        """
        Lists YAFFS2 file system objects based on filtering and versioning options.
        
        This method can operate in two modes:
          - `last_only`: Lists only the most recent version of each object.
          - Full history: Lists all versions of all objects, filtered by various criteria.
        
        Args:
            opt (dict): Dictionary of filter and display options. Supported keys include:
                - wide (bool): Not used internally; reserved for display formatting.
                - name (str): Only include objects with this exact name.
                - last_only (bool): If True, only include the most recent version of each object.
                - snapshot (int): Optional UNIX timestamp to restrict selection to objects created before or at this time.
                - obj_ids (list[int]): List of specific object IDs to include.
                - obj_id_from (int): Lower bound of object ID range (inclusive).
                - obj_id_to (int): Upper bound of object ID range (inclusive).
                - versions (list[int]): Specific version numbers to include.
                - version_from (int): Lower bound of version number (inclusive).
                - version_to (int): Upper bound of version number (inclusive).
        
        Returns:
            list[dict]: A list of dictionaries representing YAFFS2 file objects and their metadata. Each dictionary contains:
                - object_id, name, alias, version_num
                - parent_obj_id, filename, parent_path
                - mode, mode_brut, rdev_major, rdev_minor
                - size, uid, gid, ctime, yst_ctime, atime, mtime
                - sequence, offset, sha1
        """
        opt['wide']          = opt['wide']            if 'wide'           in opt else None
        opt['name']          = opt['name']            if 'name'           in opt else None
        opt['last_only']     = opt['last_only']       if 'last_only'      in opt else None
        opt['snapshot']      = opt['snapshot']        if 'snapshot'       in opt else None
        opt['obj_ids']       = opt['obj_ids']         if 'obj_ids'        in opt else None
        opt['obj_id_from']   = opt['obj_id_from']     if 'obj_id_from'    in opt else None
        opt['obj_id_to']     = opt['obj_id_to']       if 'obj_id_to'      in opt else None
        opt['versions']      = opt['versions']        if 'versions'       in opt else None
        opt['version_from']  = opt['version_from']    if 'version_from'   in opt else None
        opt['version_to']    = opt['version_to']      if 'version_to'     in opt else None
        
        allObj=[]
        
        for object_id, header_versions in self.headers.items():
            ############################################################################
            #  LAST_ONLY
            ############################################################################
            if opt['last_only'] is not None and opt['last_only']:
                
                header = None
                if opt['snapshot']:
                    
                    header_versions.sort(key=lambda h: (h["sequence"], h["offset"]))
                    for version_num, head in enumerate(header_versions, start=0):
                        if head['ctime'] <= opt['snapshot']:
                            header = head
                        else:
                            break
                    if header is None:
                        continue
                else:
                    # retains the more recent header according (sequence + offset)
                    header = max(header_versions, key=lambda x: (x['sequence'], x['offset']))
                    
                name        = header['name']
                #==============================================
                # name filter
                #==============================================
                if opt['name'] and header["name"] != opt['name']:
                    continue
                
                file_size   = header['size']
                max_seq     = header["sequence"]
                max_offset  = header["offset"]
                if header["deleted"]:
                    continue
                
                # Get the more recent data_chunks for each chunk_id
                (assembled, sha1) = self.get_data({
                       'data_chunks': self.data_chunks,
                       'object_id'  : object_id,
                       'max_seq'    : None,
                       'max_offset' : None,
                       'file_size'  : file_size
                })
                
                
                version_num     = 'last'
                parent_path     = self.__reconstruct_path(header["parent_obj_id"], header["yst_ctime"])
                version_name    = f"{header["visu_name"]}"
                output_path     = os.path.join('', parent_path, version_name)
                if name:
                    allObj.append({
                        'object_id':        object_id,
                        'name':             name,
                        'alias':            header['alias'],
                        'version_num':      version_num,
                        'parent_obj_id':    header['parent_obj_id'],
                        'filename':         output_path,
                        'parent_path':      parent_path,
                        'mode':             header['mode'],
                        'mode_brut':        header['mode_brut'],
                        'rdev_major':       header['rdev_major'],
                        'rdev_minor':       header['rdev_minor'],
                        'size':             header['size'],
                        'uid':              header['uid'],
                        'gid':              header['gid'],
                        'ctime':            header['ctime'],
                        'yst_ctime':        header['yst_ctime'],
                        'atime':            header['atime'],
                        'mtime':            header['mtime'],
                        'sequence':         header['sequence'],
                        'offset':           header['offset'],
                        'sha1':             sha1,
                    })
            
            ############################################################################
            #  ALL VERSIONS
            ############################################################################
            else:
                # order header_version according (sequence + offset)
                header_versions.sort(key=lambda h: (h["sequence"], h["offset"]))
                
                for version_num, header in enumerate(header_versions, start=0):
                    
                    if header["obj_type"] == 1 and version_num == 0:  # to remove the empty file creation
                        continue
                    
                    #=================================
                    # object_id filter
                    #=================================
                    if not self.__is_object_id_selected(object_id, opt['obj_ids'], opt['obj_id_from'], opt['obj_id_to']):
                        continue
                    
                    #=================================
                    # version_num filter
                    #=================================
                    if not self.__is_version_selected(version_num, opt['versions'], opt['version_from'], opt['version_to']):
                        continue
                        
                    #==============================================
                    # name filter
                    #==============================================
                    if opt['name'] and header["name"] != opt['name']:
                        continue
                    
                    
                    name        = header["name"]
                    file_size   = header["size"]
                    max_seq     = header["sequence"]
                    max_offset  = header["offset"]
                    
                    prev_parent = header_versions[version_num - 1]["parent_obj_id"] if version_num > 0 else header["parent_obj_id"]
                    moved = prev_parent != header["parent_obj_id"]
                    
                    # get data to calculate sha1
                    (assembled, sha1) = self.get_data({
                           'data_chunks': self.data_chunks,
                           'object_id'  : object_id,
                           'max_seq'    : max_seq,
                           'max_offset' : max_offset,
                           'file_size'  : file_size
                    })
                    
                    parent_path     = self.__reconstruct_path(header["parent_obj_id"], header["yst_ctime"])
                    moved_suffix    = ".moved" if moved and not header["deleted"] else ""
                    version_name    = f"{header["visu_name"]}{moved_suffix}"
                    output_path     = os.path.join('', parent_path, version_name)
                    if name:
                        allObj.append({
                            'object_id':        object_id,
                            'name':             name,
                            'alias':            header['alias'],
                            'version_num':      version_num,
                            'parent_obj_id':    header['parent_obj_id'],
                            'filename':         output_path,
                            'parent_path':      parent_path,
                            'mode':             header['mode'],
                            'mode_brut':        header['mode_brut'],
                            'rdev_major':       header['rdev_major'],
                            'rdev_minor':       header['rdev_minor'],
                            'size':             header['size'],
                            'uid':              header['uid'],
                            'gid':              header['gid'],
                            'ctime':            header['ctime'],
                            'yst_ctime':        header['yst_ctime'],
                            'atime':            header['atime'],
                            'mtime':            header['mtime'],
                            'sequence':         header['sequence'],
                            'offset':           header['offset'],
                            'sha1':             sha1,
                        })
        return allObj
    
    
    def get_data (self, opt):           # ← get data of an object id
        """
        Assembles file content from YAFFS2 data chunks for a specific object.
        
        This function reconstructs the most recent (valid) version of a file based on the
        sequence numbers and offsets of its data chunks. It supports both unbounded and
        bounded restoration scenarios, depending on the presence of `max_seq` and `max_offset`.
        
        Args:
            opt (dict): Options and metadata for the file, may contain:
                - 'data_chunks' (dict): Mapping of object_id to their data chunks.
                - 'object_id' (int): ID of the file object to extract.
                - 'max_seq' (int, optional): Maximum sequence number to include.
                - 'max_offset' (int, optional): Maximum offset value to include.
                - 'file_size' (int): Target size of the assembled file.
        
        Returns:
            tuple:
                - bytes: The assembled content of the file.
                - str: The SHA-1 checksum of the assembled content.
        """
        opt['data_chunks']  = opt['data_chunks']    if 'data_chunks'    in opt else []
        opt['object_id']    = opt['object_id']      if 'object_id'      in opt else 0
        opt['max_seq']      = opt['max_seq']        if 'max_seq'        in opt else None
        opt['max_offset']   = opt['max_offset']     if 'max_offset'     in opt else self.total_file_size
        opt['file_size']    = opt['file_size']      if 'file_size'      in opt else 0
        version_chunks = {}
        if opt['max_seq']:
            for chunk in opt['data_chunks'].get(opt['object_id'], []):
                cid = chunk["chunk_id"]
                if cid in version_chunks:
                    # Replace if more recent
                    prev = version_chunks[cid]
                    if (chunk["sequence"], chunk["offset"]) > (prev["sequence"], prev["offset"]):
                        if (chunk["sequence"] < opt['max_seq'] or (chunk["sequence"] == opt['max_seq'] and chunk["offset"] <= opt['max_offset'])):
                            version_chunks[cid] = chunk
                else:
                    if (chunk["sequence"] < opt['max_seq'] or (chunk["sequence"] == opt['max_seq'] and chunk["offset"] <= opt['max_offset'])):
                        version_chunks[cid] = chunk
            
        else:
            for chunk in self.data_chunks.get(opt['object_id'], []):
                cid = chunk["chunk_id"]
                if cid not in version_chunks:
                    version_chunks[cid] = {
                        'sequence': chunk['sequence'],
                        'offset':   chunk['offset'],
                        'position': chunk['position'],
                        'length':   chunk['length'],
                    }
                else:
                    old_seq     = version_chunks[cid]['sequence']
                    old_offset  = version_chunks[cid]['offset']
                    if (chunk['sequence'], chunk['offset']) > (old_seq, old_offset):
                        version_chunks[cid] = { 
                            'sequence': chunk['sequence'],
                            'offset':   chunk['offset'],
                            'position': chunk['position'],
                            'length':   chunk['length'],
                        }
        allData = []
        # Reconstitute the datas by chunk_id ascending
        for cid in sorted(version_chunks.keys()):
            position    = version_chunks[cid]['position']
            length      = version_chunks[cid]['length']
            # modify file position
            self.handle.seek(position)
            allData.append(self.handle.read(length))
        assembled = b''.join(allData)[:opt['file_size']]
        sha1            = hashlib.sha1(assembled).hexdigest()
        return assembled, sha1
    
    
    def restore_obj(self, opt, assembled, last_only, restore_right, restore_owner, outdir='.', remove_path=''):
        """
        Restores an object even a special object (directory, symlink, device, etc.) from YAFFS2 metadata.
        
        Based on the object type in `opt['mode']`, this method reconstructs the correct filesystem
        object with proper metadata and contents.
        
        Args:
            opt (dict): Metadata describing the object to restore, must contain keys like:
                        'mode', 'filename', 'parent_path', 'object_id', 'version_num', etc.
            assembled (bytes): The binary content to write into the file (if applicable).
            last_only (bool): Whether to restore only the last version (no version suffix in name).
            restore_right (bool): If True, restores file permissions (chmod).
            restore_owner (bool): If True, restores file ownership (chown, requires root).
            outdir (str, optional): Base output directory where files should be restored. Defaults to '.'.
            remove_path (str, optional): Prefix to strip from absolute symlink targets. Defaults to ''.
        
        Returns:
            str or None:
                - A warning or error message string if something failed or was skipped.
                - "Not restored" for unlinked/deleted files.
                - "Not implemented" for unsupported object types (e.g., sockets).
                - `None` if the restoration completed successfully.
        """
        self.__log(1, f"{opt['mode'][0]} | {opt['parent_path']} | {opt['filename']} | {opt['object_id']} | {opt['version_num']}")
        try:
            clean_path = outdir + '/' 
            #clean_path = path.rstrip('/')
            
            basename    = os.path.basename(opt['filename'])
            parent_dir  = os.path.dirname(opt['filename'])
            exact_path  = clean_path + opt['parent_path']
            exact_path  = exact_path.rstrip('/')
            if exact_path not in self.directories_created:
                self.__log(1, f"Creation directory : {exact_path}")
                os.makedirs(exact_path, exist_ok=True)
                self.directories_created[exact_path] = 1
            
            if basename in ('unlinked', 'deleted'):
                return "Not restored"
            
            createFile=True
            if opt['mode'][0] == '-':                    # a file
                if last_only:              # if last_only -> no version in the name
                    exact_path=clean_path + parent_dir + '/' + basename
                else:
                    exact_path=clean_path + parent_dir + '/' + basename + f".o{opt['object_id']}.v{opt['version_num']}"
                self.__log(1, f"        creating file {exact_path}...")
                
            elif opt['mode'][0] == 'd':                  # a directory
                exact_path = clean_path + parent_dir + '/' + basename
                exact_path = exact_path.rstrip('/')
                if exact_path not in self.directories_created:
                    self.__log(1, f"        creating directory {exact_path}...")
                    os.makedirs(exact_path, exist_ok=True)
                    self.directories_created[exact_path] = 1
                createFile=False
                
            elif opt['mode'][0] == 'p':                  # a named pipe
                exact_path = clean_path + parent_dir + '/' + opt['name']
                if not last_only:              # if last_only -> no version in the name
                    exact_path += f".o{opt['object_id']}.v{opt['version_num']}"
                self.__log(1, f"        creating fifo {exact_path}...")
                os.mkfifo(exact_path, opt['mode_brut'])
                createFile=False
                
            elif opt['mode'][0] in ('b', 'c'):           # a bloc/char device
                opt['parent_path'] = self.__reconstruct_path(opt["parent_obj_id"], opt["yst_ctime"])
                exact_path = clean_path + parent_dir + '/' + opt['name']
                if not last_only:              # if last_only -> no version in the name
                    exact_path += f".o{opt['object_id']}.v{opt['version_num']}"
                self.__log(1, f"        creating bloc/char device {exact_path} with major:{opt['rdev_major']} minor:{opt['rdev_minor']} ...")
                dev = os.makedev(opt['rdev_major'], opt['rdev_minor'])
                os.mknod(exact_path, opt['mode_brut'], dev)
                createFile=False
            elif opt['mode'][0] == 'l':                  # a symlink
                source, target = self.__restore_symlink({
                    'link_path':    opt['parent_path'] + '/' + opt['name'],
                    'target':       opt['alias'],
                    'remove_path':  remove_path,
                    'outdir':       outdir
                })
                createFile=False
            else:                                       # a socket
                return "Not implemented"
            
            if createFile:
                fd = os.open(exact_path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC)
                with os.fdopen(fd, "wb") as out:
                    out.write(assembled)
            
            try:
                if restore_right:
                    os.chmod(exact_path, opt['mode_brut'])
            except Exception as e:
                return f"Chmod failed {e}"
            
            try:
                if restore_owner:
                    if os.geteuid() == 0:
                        os.chown(exact_path, opt['uid'], opt['gid'])
                    else:
                        return "WARN You must be root to chown this."
            except Exception as e:
                return f"Chown failed {e}"
                
            return None
        except Exception as e:
            return e
    
    
    def extract_yaffs_headers(self):    # ← metadatas extraction
        """
        Parses a YAFFS2 NAND image and extracts metadata headers and data chunks.
        
        This method iterates through the entire image, reading chunks consisting of a data part
        and an OOB (out-of-band) part. It identifies and stores:
            - Header chunks (file metadata)
            - Data chunks (file content)
            - Orphaned or deleted headers
        
        It also performs filtering, handles name resolution, reconstructs full paths, and 
        keeps track of SHA1 hashes of file contents when needed.
        
        Returns:
            Tuple[Dict[int, List[Dict]], Dict[int, List[Dict]], Dict[int, Dict]]:
                - headers: A dictionary mapping object IDs to a list of header versions (metadata).
                - data_chunks: A dictionary mapping object IDs to a list of data chunk metadata.
                - objects: A dictionary mapping object IDs to a summary of reconstructed file info.
        """
        index   = 0
        offset  = 0
        position= 0
        try:
            # Repositionning handle at the beginning 
            self.handle.seek(0)
            while True:
                try:
                    data    = self.handle.read(self.pagesize)
                    oob     = self.handle.read(self.oobsize)
                    if not data or not oob or len(oob) != self.oobsize or len(data) != self.pagesize:
                        break
                    
                    result = self.__parse_data_safe(oob, mylayout='oob', to_analyze=True)
                    if not result.success:
                        thisoffset = self.handle.tell() - self.pagesize - self.oobsize
                        self.__log(0, f"[Offset {thisoffset}] parse_data failed: {result.error}")
                        continue
                    spare, spare_analyze = result.data
                    
                    debug_data={}           # for debug only (see below)
                    header_analysis=''
                    if self.SEQUENCE_NUMBER[0] <= spare['sequence_number'] <= self.SEQUENCE_NUMBER[1]:            # sequence_number should be [0x00001000 - 0xEFFFFF00] according yaffs_guts.h 
                        
                        if spare['chunk_id'] == 0:        # Header chunk
                            if spare['obj_type'] in self.OBJECT_TYPE_ID:
                                
                                result = self.__parse_data_safe(data, mylayout='data', to_analyze=True)
                                if not result.success:
                                    thisoffset = self.handle.tell() - self.pagesize - self.oobsize
                                    self.__log(0, f"[Offset {thisoffset}] parse_data failed: {result.error}")
                                    continue
                                dat, header_analysis = result.data
                                
                                if spare['has_packed_data'] and spare['n_bytes']:
                                    dat['file_size'] = spare['n_bytes']
                                dat['name']     = dat['name'].decode('utf-8', errors='ignore')
                                dat['alias']    = dat['alias'].decode('utf-8', errors='ignore')
                                is_deleted = (int(spare['parent_obj_id']) in self.SPECIAL_PARENT_ID and int(spare['parent_obj_id']) > 1)
                                
                                # Remember the object structure and his versionning
                                self.objects[spare['object_id']].append({
                                    "name"          : dat['name'],
                                    "yst_ctime"     : dat['yst_ctime'],
                                    "parent_id"     : int(spare['parent_obj_id']),
                                    "type"          : spare['obj_type'],
                                })
                                dat['visu_name'] = dat['name']
                                if spare['obj_type'] in (2, 4):     # links
                                    dat['visu_name'] = dat['name'] + ' -> ' + dat['alias']
                                
                                # Orphan management
                                if spare['object_id'] in self.headers and self.headers[spare['object_id']][0]['orphan']:
                                    del self.headers[spare['object_id']][0]
                                
                                self.headers[spare['object_id']].append({
                                    "chunk_id"      : int(spare['chunk_id']),
                                    "visu_name"     : dat['visu_name'],
                                    "index"         : index,
                                    "sequence"      : int(spare['sequence_number']),
                                    "mode"          : self.__mode_to_rwx(dat['yst_mode_brut'], self.OBJECT_MODE[dat['yst_type_file']]),
                                    "mode_brut"     : dat['yst_mode'],
                                    "type_obj"      : dat['yst_type_file'],
                                    "size"          : int(dat['file_size']),
                                    "uid"           : dat['yst_uid'],
                                    "gid"           : dat['yst_gid'],
                                    "rdev_major"    : dat['yst_rdev_major'],
                                    "rdev_minor"    : dat['yst_rdev_minor'],
                                    'yst_ctime'     : dat['yst_ctime'],
                                    "ctime"         : self.__format_time(dat['yst_ctime']),
                                    "mtime"         : self.__format_time(dat['yst_mtime']),
                                    "atime"         : self.__format_time(dat['yst_atime']),
                                    "parent_obj_id" : int(spare['parent_obj_id']),
                                    "offset"        : offset,
                                    "deleted"       : is_deleted,
                                    'obj_type'      : spare['obj_type'],
                                    "alias"         : dat['alias'],
                                    "name"          : dat['name'],
                                    "blockstate"    : spare['blockstate'],
                                    "bs_signif"     : spare['bs_signif'],
                                    "orphan"        : False,
                                })
                                debug_data = dat        # for debug only (see below)
                                
                        elif spare['chunk_id'] > 0:
                            self.data_chunks[spare['object_id']].append({
                                "chunk_id"      : int(spare['chunk_id']),
                                "sequence"      : int(spare['sequence_number']),
                                "offset"        : offset,
                                "position"      : index * (self.pagesize + self.oobsize),
                                "length"        : spare['n_bytes'],
                                "index"         : index,
                            })
                            debug_data={'data_size': spare['n_bytes'], "data": f"*** see above in hexadecimal dumped data, starting at the beginning of data part, for {spare['n_bytes']} bytes ***"}
                            # If we do not has already seen a header chunk concerning that object_id, create dummy one (orphan)
                            if spare['object_id'] not in self.headers:
                                self.headers[spare['object_id']].append({
                                    "chunk_id"      : 0,
                                    "visu_name"     : 'orphan',
                                    "index"         : index,
                                    "sequence"      : int(spare['sequence_number']),
                                    "mode"          : '-rw-r--r--',
                                    "mode_brut"     : self.DEFAULT_MODE,
                                    "type_obj"      : 1,
                                    "size"          : spare['n_bytes'],
                                    "uid"           : 0,
                                    "gid"           : 0,
                                    "rdev_major"    : 0,
                                    "rdev_minor"    : 0,
                                    'yst_ctime'     : self.DEFAULT_CTIME,
                                    "ctime"         : self.__format_time(1),
                                    "mtime"         : self.__format_time(1),
                                    "atime"         : self.__format_time(0),
                                    "parent_obj_id" : self.ROOT_PARENT_ID,
                                    "offset"        : offset,
                                    "deleted"       : True,
                                    'obj_type'      : spare['blockstate'],
                                    "alias"         : '',
                                    "name"          : 'orphan',
                                    "blockstate"    : spare['blockstate'],
                                    "bs_signif"     : spare['bs_signif'],
                                    "orphan"        : True,
                                })
                            elif self.headers[spare['object_id']][0]['orphan']:
                                self.headers[spare['object_id']][0]['size']  += spare['n_bytes']
                                self.headers[spare['object_id']][0]['offset'] = offset
                                if self.headers[spare['object_id']][0]['sequence'] < int(spare['sequence_number']):
                                    self.headers[spare['object_id']][0]['sequence'] = int(spare['sequence_number'])
                                
                    else:
                        spare['obj_type_name']="EMPTY CHUNK"
                        spare['obj_type']=-1
                    
                    #------------------------------------------------------------------------------
                    #-----------------------[ Debug level 2 ]--------------------------------------
                    
                    if self.debug >= 2:
                        if spare['obj_type_name'] is not None:
                            self.__log(0, "\n\n\n\n========================================================================================================================================")
                            self.__log(0, f"CHUNK #{index:>08d}        ||  Object type {spare['obj_type_name']:>27} ({spare['obj_type']:2})  ||")
                            self.__log(0, f"{spare['bs_signif']:<22} ++================================================++ {spare['bs_signif']:>22}\n")
                            head = [
                                f"---[ data part ]--- ",
                                f"size: {self.pagesize} bytes",
                            ]
                            trai = []
                            self.__hexdump(data,  start_offset=position, left=head, right=trai)
                            self.__log(0, f"\n                                ........................[ Analyze ]........................")
                            self.__log(0, f"{header_analysis}")
                            self.__log(0, f"\n")
                            self.__log(0, f"result = {debug_data}")
                            self.__log(0, "\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
                            self.__log(0, "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n")
                            head = [
                                f"---[  oob part ]--- ",
                                f"size: {self.oobsize} bytes",
                            ]
                            trai = []
                            self.__hexdump(oob,   start_offset=position + self.pagesize, left=head, right=trai)
                            self.__log(0, f"\n                                ........................[ Analyze ]........................")
                            self.__log(0, f"{spare_analyze}")
                            self.__log(0, f"\n")
                            self.__log(0, f"result = {spare}")
                    #-----------------------[/ Debug level 2 ]--------------------------------------
                    
                    offset = self.handle.tell() - self.total_chunk_size
                    position = self.handle.tell()
                    index += 1
                except Exception as e:
                    theoffset = self.handle.tell()
                    self.__log(0, f"[Offset {theoffset}] Read failed : {e}")
                    break
            self.total_file_size = position
            return (self.headers, self.data_chunks, self.objects)
            
        except Exception as e:
            self.__log(0, f"Unknown error : {e}")
        
        return (defaultdict(list), defaultdict(list), defaultdict(list))
    
    
    def parse_data(self, data=b'', mylayout='oob', to_analyze = False):
        """
        Parses a binary block using either the OOB or DATA layout, depending on context.
        
        This function interprets a block of raw bytes (OOB or DATA), extracts structured fields
        based on predefined layouts, and optionally returns a debug string of the interpretation.
        
        Args:
            data (bytes): The raw binary block to parse.
            mylayout (str): Specifies which layout to use. 
                - 'oob' uses self.OOB_LAYOUT.
                - 'data' uses self.DATA_LAYOUT.
            to_analyze (bool): If True, returns an analysis string showing decoded fields for debug purposes.
        
        Returns:
            tuple:
                dict: A dictionary containing parsed fields and interpretation results.
                str: (Optional) A debug string representation of parsed content if `to_analyze` is True.
        
        Notes:
            - In 'oob' mode, this function also attempts to deduce object type, validity, and special flags.
            - In 'data' mode, it extracts file metadata including permissions, name, and size.
            - The function supports both little and big endian byte orders.
        """
        if mylayout=='oob':
            dic={
                'obj_type'          : None,
                'parent_obj_id'     : None,
                'has_packed_data'   : False,
            }
            mylist = self.OOB_LAYOUT
        else:
            dic={
                'file_size'      : 0,
            }
            mylist = self.DATA_LAYOUT
        analyze=''
        for obj in mylist:
            k   = obj['field']
            pos = obj['pos']
            
            valeur = data[pos[0]:pos[0] + pos[1]]
            
            if to_analyze:
                analyze += f"                                {k:20s}    {pos} -> {self.__dump_bytes(valeur)}\n"
            if self.endianness == 'little':         # little endian
                if pos[1] == 1:
                    dic[k] = struct.unpack("<B", valeur)[0]
                elif pos[1] == 2:
                    dic[k] = struct.unpack("<H", valeur)[0]
                elif pos[1] == 4:
                    dic[k] = struct.unpack("<I", valeur)[0]
                else:
                    dic[k] = valeur
            else:                                   # big endian
                if pos[1] == 1:
                    dic[k] = struct.unpack(">B", valeur)[0]
                elif pos[1] == 2:
                    dic[k] = struct.unpack(">H", valeur)[0]
                elif pos[1] == 4:
                    dic[k] = struct.unpack(">I", valeur)[0]
                else:
                    dic[k] = valeur
                
        if mylayout=='oob':
            dic['obj_type']         = int.from_bytes(struct.pack("<I", dic['object_id'] >> 28), byteorder='little')
            dic['obj_type_name']    = None
            dic['bs_signif']        = "GOOD Chunk"
            if dic['blockstate'] != 255:
                dic['bs_signif'] = "!!! BAD Chunk !!!"
            if dic['obj_type'] in self.OBJECT_TYPE_ID:           #>> if obj_type is known ... then it has a name
                dic['obj_type_name'] = self.OBJECT_TYPE_ID[dic['obj_type']]
            if dic['chunk_id'] & 0x80000000:        # Does the most significant byte is 8 ?
                dic['object_id']        = dic['object_id'] & ~(0x0f << 28)      # only keep the most significant byte
                dic['parent_obj_id']    = dic['chunk_id'] & 0x0FFFFFFF          # remove the most significant byte
                dic['has_packed_data']  = True
                dic['chunk_id']         = 0
                dic['file_size']        = dic['n_bytes']
            elif dic['chunk_id'] & 0xC0000000:      # it's a hole (not managed in this software)
                dic['has_packed_data']  = False
                
        else:
            (dic['yst_mode_brut'], dic['yst_type_file'])    = self.__split_mode(dic['yst_mode'])           # get file permission and file type (usefull for __mode_to_rwx function)
            (dic['yst_rdev_major'], dic['yst_rdev_minor'])  = self.__extract_major_minor(dic['yst_rdev'])
            dic['name']                                     = self.__null_terminate_string(dic['name'])
            dic['alias']                                    = self.__null_terminate_string(dic['alias'])
            if dic['file_size_high'] != 0xFFFFFFFF:
                dic['file_size'] = dic['file_size_low'] | (dic['file_size_high'] << 32)     # merge file_size_high | file_size_low
            elif dic['file_size_low'] != 0xFFFFFFFF:
                dic['file_size'] = dic['file_size_low']
            else:
                dic['file_size'] = 0
        return dic, analyze
    
    
    def get_params (self):              # ← get config
        """
        Returns the current parameters of the YAFFS2 image being analyzed.
        
        Returns:
            dict: A dictionary containing:
                - 'pagesize' (int): The size of each data page.
                - 'oobsize' (int): The size of the out-of-band (OOB) area.
                - 'endianness' (str): The endianness used ('little' or 'big').
        """
        return ({
            'pagesize':     self.pagesize,
            'oobsize':      self.oobsize,
            'endianness':   self.endianness
        })
    
    
    # === Private Helpers ===
    def __del__(self):
        """Destructor for the Yaffs2Forensic class. Ensures cleanup if needed."""
        print('Yaffs2Forensic Destructor called')
    
    
    def __close(self):
        """Closes the image file handle if it is open."""
        if self.handle and not self.handle.closed:
            self.handle.close()
    
    
    def __enter__(self):
        """
        Enables the use of the class in a context manager (`with` statement).
        
        Returns:
            Yaffs2Forensic: The current instance.
        """
        return self
    
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Called when exiting a `with` block. Ensures the file is closed.
        
        Args:
            exc_type (type): The exception type (if any).
            exc_val (Exception): The exception instance (if any).
            exc_tb (traceback): The traceback object (if any).
        """
        self.__close()
    
    
    def __log(self, level, message):
        """
        Internal logging function based on debug level.
        
        Args:
            level (int): The required debug level to display the message.
            message (str): The message to be printed.
        """
        if self.debug >= level:
            print(message)
    
    
    def __format_time(self, ts):
        """
        Converts a UNIX timestamp to a human-readable datetime string.
        
        Args:
            ts (int or float): The timestamp in epoch seconds.
        
        Returns:
            str: A formatted date-time string, or '?' if the conversion fails.
        """
        try:
            return datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        except:
            return "?"
    
    
    def __hexdump(self, data, start_offset=0, left=None, right=None):
        """
        Prints a formatted hexdump of the given data, optionally with aligned left and right annotations.
        
        Args:
            data (bytes or str): The binary data to display. If a string is provided, it will be encoded in UTF-8.
            start_offset (int, optional): Starting offset to display alongside the hex lines. Defaults to 0.
            left (list[str], optional): Optional annotations to display on the left of each line.
            right (list[str], optional): Optional annotations to display on the right of each line.
        
        Notes:
            This method uses __log to output lines with aligned hexadecimal and ASCII views of the data.
        """
        if isinstance(data, str):
            data = data.encode('utf-8')
        
        if left is None:
            left = []
        if right is None:
            right = []
        
        length = 16
        total_lines = (len(data) + length - 1) // length
        
        # Get the header max length
        max_header_width = max((len(h) for h in left), default=0)
        
        for line_idx in range(total_lines):
            offset = start_offset + line_idx * length
            chunk = data[line_idx * length:(line_idx + 1) * length]
            
            hex_bytes = ' '.join(f"{b:02x}" for b in chunk).ljust(3 * length - 1)
            hex_bytes = hex_bytes[:8*3-1] + '  ' + hex_bytes[8*3-1:]
            
            ascii_repr = ''.join(chr(b) if 32 <= b <= 126 else '.' for b in chunk)
            
            header_str = left[line_idx] if line_idx < len(left) else ''
            trailer_str = right[line_idx] if line_idx < len(right) else ''
            
            padded_header = header_str.ljust(max_header_width)
            
            self.__log(0, f"{padded_header}{offset:08x}  {hex_bytes}  |{ascii_repr}|{trailer_str}")
    
    
    def __dump_bytes(self, the_bytes):
        """
        Converts a sequence of bytes into a string of hexadecimal escape sequences.
        
        Args:
            the_bytes (bytes): A bytes object to convert.
        
        Returns:
            str: A string representation with escaped hex values, e.g., '\\x4f\\x6b '.
        """
        return (''.join(f'\\x{b:02x} ' for b in the_bytes))
    
    
    def __null_terminate_string(self, string):
        """
        Truncates a byte string at the first null byte (0x00), emulating C-style null-terminated strings.
        
        Args:
            string (bytes): The input byte string.
        
        Returns:
            bytes: The truncated string, ending before the first null byte, or the full string if no null byte is found.
        """
        try:
            i = string.index(b'\x00')
        except Exception as e:
            i = len(string)
        return string[0:i]
    
    
    def __mode_to_rwx(self, mode, cste):
        """
        Converts a file mode integer into a symbolic 'rwx' string.
        
        Args:
            mode (int): The permission bits and type of the file.
            cste (int): A bitmask constant to OR with the mode before conversion.
        
        Returns:
            str: A symbolic representation of the mode (e.g., '-rw-r--r--'), or "???" if the input is invalid.
        """
        mode = cste | mode
        return stat.filemode(mode) if isinstance(mode, int) else "???"
    
    
    def __extract_major_minor(self, rdev):
        """
        Extracts the major and minor numbers from a raw device ID.
        
        Args:
            rdev (int): The raw device number, typically from a YAFFS2 metadata field.
        
        Returns:
            tuple: A tuple (major, minor) representing the device's major and minor numbers.
        """
        major = (rdev >> 8) & 0xFF
        minor = rdev & 0xFF
        return major, minor
    
    
    def __split_mode(self, mode):
        """
        Splits a raw mode integer into Unix-style permission bits and a type identifier.
        
        Args:
            mode (int): The raw mode value combining permission bits and file type (e.g., from stat).
        
        Returns:
            tuple: A tuple (permissions, typenum) where:
                - permissions (int): Unix-style permission bits (e.g., 0o755).
                - typenum (int): Mapped type identifier:
                    1 = regular file,
                    2 = symlink,
                    3 = directory,
                    5 = char device,
                    6 = block device,
                    7 = FIFO,
                    8 = socket,
                    0 = unknown type.
        """
        # Extract type file
        file_type = stat.S_IFMT(mode)  # mask permissions bits
        # Extract permissions (bits 0 à 11)
        permissions = mode & 0o7777
        # Mapping type_file (see variable OBJECT_MODE)
        if file_type == stat.S_IFREG:
            typenum = 1
        elif file_type == stat.S_IFDIR:
            typenum = 3
        elif file_type == stat.S_IFLNK:
            typenum = 2
        elif file_type == stat.S_IFCHR:
            typenum = 5
        elif file_type == stat.S_IFBLK:
            typenum = 6
        elif file_type == stat.S_IFIFO:
            typenum = 7
        elif file_type == stat.S_IFSOCK:
            typenum = 8
        else:
            typenum = 0
        return permissions, typenum
    
    
    def __parse_data_safe(self, data=b'', mylayout='oob', to_analyze=True):
        """
        Safely parses a YAFFS data or OOB block, catching any exception.
        
        This method acts as a protective wrapper around `parse_data()`. If any error
        occurs during parsing, it returns a `Result` object with the error instead of raising.
        
        Args:
            data (bytes, optional): The binary block to parse. Defaults to an empty byte string.
            mylayout (str, optional): Layout type to use ('data' or 'oob'). Defaults to 'oob'.
            to_analyze (bool, optional): Whether to run deep analysis on the parsed block. Defaults to True.
        
        Returns:
            Result: An object with the following attributes:
                - success (bool): True if parsing succeeded, False otherwise.
                - data (dict): The parsed data if successful.
                - error (str): Error message if parsing failed.
        """
        try:
            parsed = self.parse_data(data, mylayout=mylayout, to_analyze=to_analyze)
            return self.Result(True, data=parsed)
        except Exception as e:
            return self.Result(False, error=str(e))
    
    
    def __reconstruct_path(self, obj_id, yst_ctime):
        """
        Reconstructs the full path of a YAFFS2 object based on its object ID and creation time.
        
        This method walks back the hierarchy of parent objects from a given object ID,
        selecting the directory names that were valid at the specified creation timestamp.
        This allows versioned path reconstruction.
        
        Args:
            obj_id (int): The object ID of the target file or directory.
            yst_ctime (int): The creation time (epoch) to consider for versioning.
        
        Returns:
            str: The full reconstructed path, or an empty string if not found.
        """
        parts = []
        while obj_id in self.objects and obj_id != 1:
            obj = self.objects[obj_id]
            kept = obj[0]
            for version_num, head in enumerate(obj, start=0):
                if head['yst_ctime'] <= yst_ctime:
                    kept = head
                else:
                    break
            parts.insert(0, kept["name"])
            obj_id = kept["parent_id"]
        return os.path.join(*parts) if parts else ""
    
    
    def __is_object_id_selected(self, object_id, obj_ids, obj_id_from, obj_id_to):
        """
        Checks if the given object ID is selected based on filters.
        
        Selection is based on:
        - Inclusion in a list of specific object IDs.
        - Being within a defined range of object IDs.
        - If no filters are defined, all object IDs are selected.
        
        Args:
            object_id (int): The object ID to check.
            obj_ids (list[int] or None): List of explicitly selected object IDs.
            obj_id_from (int or None): Start of the object ID range.
            obj_id_to (int or None): End of the object ID range.
        
        Returns:
            bool: True if the object ID matches the filter criteria.
        """
        if obj_ids and object_id in obj_ids:
            return True
        if obj_id_from is not None and obj_id_to is not None:
            if obj_id_from <= object_id <= obj_id_to:
                return True
        if not obj_ids and obj_id_from is None and obj_id_to is None:
            return True  # No filter applied
        return False
    
    
    def __is_version_selected(self, version_num, versions, version_from, version_to):
        """
        Checks if the given version number is selected based on filters.
        
        Selection is based on:
        - Inclusion in a list of specific version numbers.
        - Being within a defined range of version numbers.
        - If no filters are defined, all versions are selected.
        
        Args:
            version_num (int): The version number to check.
            versions (list[int] or None): List of explicitly selected versions.
            version_from (int or None): Start of the version range.
            version_to (int or None): End of the version range.
        
        Returns:
            bool: True if the version number matches the filter criteria.
        """
        if versions and version_num in versions:
            return True
        if version_from is not None and version_to is not None:
            if version_from <= version_num <= version_to:
                return True
        if not versions and version_from is None and version_to is None:
            return True  # No filter applied
        return False
    
    
    def __restore_symlink(self, opt):
        """
        Restores a symbolic link using path resolution and symlink creation.
        
        Handles both absolute and relative link targets, including rewriting
        absolute paths if `remove_path` is specified. Ensures the link directory
        exists, deletes any existing link, and then creates the new one.
        
        Args:
            opt (dict): Dictionary containing:
                - 'outdir' (str): Output directory where the link should be created.
                - 'link_path' (str): Relative path of the link to restore.
                - 'target' (str): Path the symlink should point to.
                - 'remove_path' (str or None): Optional path prefix to remove from absolute targets.
        
        Returns:
            tuple: (str, str) The full source path of the symlink, and the resolved target path.
        
        Raises:
            OSError: If an error occurs during symlink creation (other than file not found).
        """
        # Path resolution
        source = os.path.join(opt['outdir'], opt['link_path'])
        source_dir = os.path.dirname(source)
        
        if os.path.isabs(opt['target']):
            if opt['remove_path'] and target.startswith(opt['remove_path']):
                target = os.path.join(opt['outdir'], os.path.relpath(opt['target'], opt['remove_path']))
        else:
            target = os.path.abspath(os.path.join(source_dir, opt['target']))
        
        # creating parent directory if needed
        os.makedirs(source_dir, exist_ok=True)
        
        # Remove the link if it exists
        try:
            os.remove(source)
        except FileNotFoundError:
            pass
        except OSError as e:
            if e.errno != errno.ENOENT:
                raise
        # Link creation
        os.symlink(target, source)
        return source, target
    
    
    
    def __is_plausible_oob(self, parsed, pagesize):
        """
        Checks whether parsed OOB (Out-Of-Band) metadata is plausible.
        
        Applies heuristic rules to determine if the OOB data corresponds to expected YAFFS2 metadata.
        
        Args:
            parsed (dict): Parsed OOB data fields.
            pagesize (int): Expected page size in bytes.
        
        Returns:
            bool: True if the data appears valid and plausible, False otherwise.
        """
        try:
            return (
                0 < parsed['object_id'] < 100000        and
                parsed['chunk_id'] >= 0                 and
                parsed['n_bytes'] <= pagesize           and
                parsed['obj_type'] in self.OBJECT_TYPE_ID    and
                self.SEQUENCE_NUMBER[0] <= parsed['sequence_number'] <= self.SEQUENCE_NUMBER[1]         # according yaffs_guts.h
            )
        except KeyError:
            return False
    
    
    def __is_plausible_data(self, parsed):
        """
        Checks whether parsed data metadata (e.g., timestamps, UID, GID) is plausible.
        
        Applies heuristic checks such as valid UID/GID ranges and UNIX timestamp boundaries.
        
        Args:
            parsed (dict): Parsed data fields (from the data section of the page).
        
        Returns:
            bool: True if the values seem plausible, False otherwise.
        """
        try:
            return (
                0 <= parsed['yst_uid'] < 65536                  and
                0 <= parsed['yst_gid'] < 65536                  and
                1000000000 < parsed['yst_atime'] < 2000000000   and
                1000000000 < parsed['yst_mtime'] < 2000000000   and
                1000000000 < parsed['yst_ctime'] < 2000000000   and
                0 <= parsed['yst_mode'] <= 0xFFFF
            )
        except KeyError:
            return False
    
    
    def __score_format(self, pagesize, oobsize, endianness, max_blocks=1000):
        """
        Scores the plausibility of a YAFFS2 format by checking the first N chunks.
        
        Parses a number of blocks using the specified `pagesize`, `oobsize`, and `endianness`,
        and scores them based on how plausible the extracted OOB and data fields are.
        
        Args:
            pagesize (int): Presumed page size in bytes.
            oobsize (int): Presumed OOB (spare area) size in bytes.
            endianness (str): Byte order used in the data ('little' or 'big').
            max_blocks (int, optional): Number of chunks to scan and score. Defaults to 1000.
        
        Returns:
            int: The total score obtained (higher = more likely to be valid format).
        """
        score = 0
        self.set_params({
            'pagesize':     pagesize,
            'oobsize':      oobsize,
            'endianness':   endianness,
        })
        try:
            # Repositionning handle at the beginning 
            self.handle.seek(0)
            offset=0
            i=0
            for _ in range(max_blocks):
                data    = self.handle.read(pagesize)
                oob     = self.handle.read(oobsize)
                if len(data) < pagesize or len(oob) < oobsize:
                    break
                
                try:
                    (parsed_oob, _) = self.parse_data(oob, mylayout='oob', to_analyze = False)    # parse the oob part
                    if self.__is_plausible_oob(parsed_oob, pagesize):
                        score += 2          # better score for oob part
                except Exception as e:
                    self.__log(1, f"Error parsing oob part of block #{i} : {e}")
                    pass
                
                try:
                    (parsed_data, _) = self.parse_data(data, mylayout='data', to_analyze = False) # parse the data part
                    if self.__is_plausible_data(parsed_data):
                        score += 1
                except Exception as e:
                    self.__log(1, f"Error parsing data part of block #{i}: {e}")
                    pass
                offset = self.handle.tell() - (pagesize + oobsize)
                i += 1
            return score
            
        except Exception as e:
            self.__log(0, f"Unknown error : {e}")
        
        return 0