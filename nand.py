import argparse
import sys
import re
from Yaffs2Forensic import Yaffs2Forensic

CANDIDATES = [
    (2048, 64),
    (4096, 128),
    (512, 16),
    (8192, 224),
    (16384, 448),
]

def log(args, level, message):
    """
    Function used to manage debug levels
    """
    if args.debug >= level:
        print(message)


def parse_args():
    """
    Parse arg function needed to manage parameters 
    """
    
    parser = argparse.ArgumentParser(
        prog='nandparser.py',
        description=(
            "This program tries to forensic a YAFFS2 partition and tries to restore as much as possible\n"
            "  --> even deleted and orphans (data chunk without metadata)\n"
            "*** If you want to restore blockdevice / chardevice or --restore_owner, run me as root ***"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter
    )


    parser.add_argument("--image", type=str, required=True,
                        help="YAFFS2 image to process/analyze")

    parser.add_argument("--obj_ids", type=int, nargs="+",
                        help="Object_id (list) to retain")

    parser.add_argument("--obj_id_from", type=int,
                        help="Minimum Object_id to retain")

    parser.add_argument("--obj_id_to", type=int,
                        help="Maximum Object_id to retain")

    parser.add_argument("--snapshot", type=str,
                        help="Reconstruct the NAND state at this timestamp (format 'YYYY-MM-DD hh:mm:ss')")

    parser.add_argument("--name", type=str,
                        help="Retain only the file specified")

    parser.add_argument("--versions", type=int, nargs="+",
                        help="Versions (list) to retain")

    parser.add_argument("--version_from", type=int,
                        help="Minimum Version number to retain")

    parser.add_argument("--version_to", type=int,
                        help="Maximum Version number to retain")

    parser.add_argument("--outdir", type=str,
                        help="Output Directory : if set, restoration will be done / "
                             "*** for [block|char]devices requires to be root ***\n"
                        )

    parser.add_argument("--debug", type=int, default=0, choices=range(0, 3),
                        help="Debug level : 0 (none), 1 (base), 2 (detailed)")

    parser.add_argument("--last_only", action="store_true",
                        help="If activated, process only the last file version. The restored files will not contain object_id and version")

    parser.add_argument("--wide", action="store_true",
                        help="If activated, wide print (much more informations)")

    parser.add_argument("--autodetect", action="store_true",
                        help="If activated, auto-detecting pagesize / oobsize / [littel|big]-endian")
    
    parser.add_argument("--autodetect_only", action="store_true",
                        help="If activated, auto-detecting pagesize / oobsize / [littel|big]-endian and stop !")

    parser.add_argument('--pagesize', type=int, default=2048,
                        help="Pagesize in bytes")

    parser.add_argument('--oobsize', type=int, default=64,
                        help="OOB size in bytes")
    
    parser.add_argument("--endianness", type=str , default='little', choices=['big', 'little'],
                        help="Little (default) or big endian")
                        
    parser.add_argument("--restore_owner", action="store_true",
                        help="If activated, restore owners *** requires to be root ***")
    
    parser.add_argument("--restore_right", action="store_true",
                        help="If activated, restore rights")
    
    parser.add_argument("--remove_path", type=str,
                        help="Only for absolute symlink : remove base path "
                            "e.g. if you have dir1/dir2/dir3/link1 --> /mnt/yaffs/test1.txt "
                            " --remove_path /mnt/yaffs will remove that string in the targer "
                            " dir1/dir2/dir3/link1 --> test1.txt "
                            "then using --outdir /tmp/toto will restore "
                            "/tmp/toto/dir1/dir2/dir3/link1 --> /tmp/toto/test1.txt"
                        )

    return parser.parse_args()


#############################################################
# Manage the coherence between given parameters 
#############################################################
args = parse_args()

# object_id_from and object_to management
if args.obj_id_from is not None and args.obj_id_to is not None:
    if args.obj_id_from > args.obj_id_to:
        log(args, 0, "Error : obj_id_from must be <= obj_id_to.")
        sys.exit(1)

# version_from and version_to management
if args.version_from is not None and args.version_to is not None:
    if args.version_from > args.version_to:
        log(args, 0, "Error : version_from must be <= version_to.")
        sys.exit(1)

# snapshot format validation
if args.snapshot:
    snapshot_regex = r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$"
    if not re.match(snapshot_regex, args.snapshot):
        log(args, 0, "Parameter --snapshot must be in the format 'YYYY-MM-DD hh:mm:ss'")
        sys.exit(1)
    try:
        args.snapshot_datetime = datetime.strptime(args.snapshot, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        log(args, 0, "Unable to parse snapshot, please check the format.")
        sys.exit(1)
    args.last_only = True

# autodetect + pagesize and oobsize management
if not args.autodetect:
    pair = (args.pagesize, args.oobsize)
    
    if pair not in CANDIDATES:
        log(args, 0, f"Error : the tupple pagesize/oobsize {pair} is invalid.")
        log(args, 0, f"Accepted values : {CANDIDATES}")
        exit(1)
        
    if args.endianness not in ("little", 'big'):
        log(args, 0, f"Error : endianness is invalid.")
        log(args, 0, f"Accepted values : {ENDIANNESS_OPTIONS}")
        exit(1)


log(args, 2, f"Arguments : {args}")
log(args, 2, "")
log(args, 2, "")




if __name__ == "__main__":
    try:
        with Yaffs2Forensic({
            'image'         : args.image,
            'debug'         : args.debug
            }) as yaffs2:
            
            
            if args.autodetect or args.autodetect_only: 
                log(args, 1, f"Auto-detecting NAND parameters ...")
                (best_score, pagesize, oobsize, endianness) = yaffs2.autodetect_format()
                yaffs2.set_params({
                    'pagesize':     pagesize,
                    'oobsize':      oobsize,
                    'endianness':   endianness,
                })
                if args.autodetect_only:
                    exit(0)
            else:
                yaffs2.set_params({
                    'pagesize':     args.pagesize,
                    'oobsize':      args.oobsize,
                    'endianness':   args.endianness,
                })
            
            params = yaffs2.get_params()
            log(args, 0, f"Processing image {args.image} with pagesize {params['pagesize']} and oobsize {params['oobsize']} in {params['endianness']}-endian ...")
            (headers, data_chunks, objects) = yaffs2.extract_yaffs_headers()
            #==============================================================================
            # Listing
            #==============================================================================
            allObj = yaffs2.list_obj({
                'wide'          : args.wide,
                'name'          : args.name,
                'last_only'     : args.last_only,
                'snapshot'      : args.snapshot,
                'obj_ids'       : args.obj_ids,
                'obj_id_from'   : args.obj_id_from,
                'obj_id_to'     : args.obj_id_to,
                'versions'      : args.versions,
                'version_from'  : args.version_from,
                'version_to'    : args.version_to,
            })
            #log(args, 0, f"{allObj}")
            if (args.wide):
                log(args, 0, f"\n{'obj.ID':>9}  {'ver.':>6}  {'parentId':>9}  {'name':<50}  {'mode':>10}  {'size':>10}  {'uid':>6}  {'gid':>6}  {'ctime':>19}  {'atime':>19}  {'mtime':>19}  {'sequence':>10}  {'offset':>10}  {'sha1sum':<8}")
                for obj in allObj:
                    log(args, 0, f"{obj['object_id']:>9}  {obj['version_num']:>6}  {obj['parent_obj_id']:>9}  {obj['filename']:<50}  {obj['mode']:>10}  {obj['size']:>10}  {obj['uid']:>6}  {obj['gid']:>6}  {obj['ctime']:>19}  {obj['atime']:>19}  {obj['mtime']:>19}  {obj['sequence']:>10}  {obj['offset']:>10}  {obj['sha1']}")
            else :
                log(args, 0, f"\n{'mode':<10}  {'uid':>6}  {'gid':>6}  {'size':>10}  {'ctime':<10}  {'obj.ID':>9}  {'ver.':>6}  {'name':<50}")
                for obj in allObj:
                    log(args, 0, f"{obj['mode']:>10}  {obj['uid']:>6}  {obj['gid']:>6}  {obj['size']:>10}  {obj['ctime'][:10]:>10}  {obj['object_id']:>9}  {obj['version_num']:>6}  {obj['filename']:<50}")
            
            #==============================================================================
            # Restoration
            #==============================================================================
            restore_suffixe=''
            if args.outdir:
                total_size=0
                total_nb=0
                total_restored_size = 0
                total_restored_nb = 0
                log(args, 0, f"\n============================================================================================================================================")
                log(args, 0, f"Restoration")
                log(args, 0, f"============================================================================================================================================")
                log(args, 0, f"\n{'mode':<10}  {'uid':>6}  {'gid':>6}  {'size':>10}  {'ctime':<10}  {'obj.ID':>9}  {'ver.':>6}  {'name':<50}")
                for obj in allObj:
                    max_seq = obj['sequence']
                    offset  = obj['offset']
                    if args.last_only is not None and args.last_only:
                        max_seq = None
                        offset  = None
                    (assembled, sha1) = yaffs2.get_data({
                       'data_chunks': data_chunks,
                       'object_id'  : obj['object_id'],
                       'max_seq'    : max_seq,
                       'max_offset' : offset,
                       'file_size'  : obj['size']
                    })
                    total_nb += 1
                    total_size += obj['size']
                    result = yaffs2.restore_obj(
                        obj,
                        assembled       = assembled,
                        last_only       = args.last_only,
                        restore_right   = args.restore_right,
                        restore_owner   = args.restore_owner,
                        outdir          = args.outdir,
                        remove_path     = args.remove_path
                    )
                    if result:
                        restore_suffixe=f" !!! Unable to restore {obj['filename']} [{result}]"
                    else:
                        total_restored_size += obj['size']
                        total_restored_nb += 1
                        restore_suffixe=" > Restored"
                    log(args, 0, f"{obj['mode']:>10}  {obj['uid']:>6}  {obj['gid']:>6}  {obj['size']:>10}  {obj['ctime'][:10]:>10}  {obj['object_id']:>9}  {obj['version_num']:>6}  {obj['filename']:<50}  {restore_suffixe}")
                log(args, 0, f"\nREPORT\n------") 
                log(args, 0, f"TOTAL {total_restored_nb}/{total_nb} restored object(s) for a total of {total_restored_size}/{total_size} bytes")
    except RuntimeError as e:
        log(args, 0, f"Erreur : {e}")