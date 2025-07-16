# YAFFS2 Forensic Toolkit

**A forensic analysis tool for YAFFS2 partitions**, enabling extraction, parsing, and inspection of data from embedded systems using the YAFFS2 file system.

## Project Structure

This repository includes:

- `yaffs2_parser.py` – Main program for YAFFS2 parsing and analysis.
- `Yaffs2Forensic.py` – Core Python class implementing YAFFS2 forensic analysis logic.
- `docs/` – Complete documentation on the YAFFS2 file system and analysis methodology.
- `test_env/` – Fully functional test environment featuring:
  - `run.sh` – Script to launch a QEMU virtual machine.
  - `initramfs.cpio.gz` – Initramfs root filesystem used by QEMU.
  - `root_container.img` – EXT2 partition image.
  - `bzImage` – Linux 3.2.0 kernel image.
- `samples/` – YAFFS2 partition snapshots for analysis and experimentation.
  - simul_1 - First pool of modifications
  - simul_2 - Second pool of modifications

## Purpose

This toolkit is designed to assist forensic analysts, reverse engineers, and security researchers in investigating raw NAND memory dumps formatted with YAFFS2. It provides tools to decode, interpret, and extract file system structures and files from embedded Linux environments.

## Requirements

- Python 3.8+
- QEMU (for the test environment)
- Linux OS (recommended for executing `run.sh`)

### Python Dependencies

No external dependencies required.

This project uses only the Python Standard Library (Python >= 3.8).

## Usage

### Analyze a YAFFS2 partition dump

```bash

usage: yaffs2_parser.py [-h] --image IMAGE [--obj_ids OBJ_IDS [OBJ_IDS ...]]
                                  [--obj_id_from OBJ_ID_FROM]
                                  [--obj_id_to OBJ_ID_TO]
                                  [--snapshot SNAPSHOT]
                                  [--name NAME]
                                  [--versions VERSIONS [VERSIONS ...]]
                                  [--version_from VERSION_FROM]
                                  [--version_to VERSION_TO]
                                  [--outdir OUTDIR]
                                  [--debug {0,1,2}]
                                  [--last_only]
                                  [--wide]
                                  [--autodetect]
                                  [--autodetect_only]
                                  [--pagesize PAGESIZE]
                                  [--oobsize OOBSIZE]
                                  [--endianness {big,little}]
                                  [--restore_owner]
                                  [--restore_right]
                                  [--remove_path REMOVE_PATH]

This program tries to forensic a YAFFS2 partition and tries to restore as much as possible
  --> even deleted and orphans (data chunk without metadata)
*** If you want to restore blockdevice / chardevice or --restore_owner, run me as root ***

options:
  -h, --help            show this help message and exit
  --image IMAGE         YAFFS2 image to process/analyze
  --obj_ids OBJ_IDS [OBJ_IDS ...]
                        Object_id (list) to retain
  --obj_id_from OBJ_ID_FROM
                        Minimum Object_id to retain
  --obj_id_to OBJ_ID_TO
                        Maximum Object_id to retain
  --snapshot SNAPSHOT   Reconstruct the NAND state at this timestamp (format 'YYYY-MM-DD hh:mm:ss')
  --name NAME           Retain only the file specified
  --versions VERSIONS [VERSIONS ...]
                        Versions (list) to retain
  --version_from VERSION_FROM
                        Minimum Version number to retain
  --version_to VERSION_TO
                        Maximum Version number to retain
  --outdir OUTDIR       Output Directory : if set, restoration will be done / **for [block|char]devices requires to be root**
  --debug {0,1,2}       Debug level : 0 (none), 1 (base), 2 (detailed)
  --last_only           If activated, process only the last file version. The restored files will not contain object_id
                        and version
  --wide                If activated, wide print (much more informations)
  --autodetect          If activated, auto-detecting pagesize / oobsize / [littel|big]-endian
  --autodetect_only     If activated, auto-detecting pagesize / oobsize / [littel|big]-endian and stop !
  --pagesize PAGESIZE   Pagesize in bytes
  --oobsize OOBSIZE     OOB size in bytes
  --endianness {big,little}
                        Little (default) or big endian
  --restore_owner       If activated, restore owners *** requires to be root ***
  --restore_right       If activated, restore rights
  --remove_path REMOVE_PATH
                        Only for absolute symlink : remove base path
                           e.g. if you have dir1/dir2/dir3/link1 --> /mnt/yaffs/test1.txt
                           --remove_path /mnt/yaffs will remove that string in the targer dir1/dir2/dir3/link1 --> test1.txt
                           then using --outdir /tmp/toto will restore
                           /tmp/toto/dir1/dir2/dir3/link1 --> /tmp/toto/test1.txt
example :

python yaffs2_parser.py --image snapshot_12_truncate_lorem_ORPHAN.bin --wide --outdir /tmp/foo 
```

This will show everything present in the YAFFS2 image and restore as much as possible in /tmp/foo

example :

```bash
#> python yaffs2_parser.py --image snapshot_12_truncate_lorem_ORPHAN.bin  --autodetect
==> Best format detected : 2048 / 64 in little-endian (score 125)
Processing image snapshot_12_truncate_lorem_ORPHAN.bin with pagesize 2048 and oobsize 64 in little-endian ...

mode           uid     gid        size  ctime          obj.ID    ver.  name                                              
-rw-r--r--       0       0           5  2025-06-05        257       1  test1.txt                                         
drwxr-xr-x       0       0           0  2025-06-05        258       0  dir1                                              
drwxr-xr-x       0       0           0  2025-06-05        258       1  dir1                                              
drwxr-xr-x       0       0           0  2025-06-05        258       2  dir1                                              
drwxr-xr-x       0       0           0  2025-06-05        258       3  dir1                                              
drwxr-xr-x       0       0           0  2025-06-05        259       0  dir1/dir2                                         
drwxr-xr-x       0       0           0  2025-06-05        259       1  dir1/dir2                                         
drwxr-xr-x       0       0           0  2025-06-05        259       2  dir1/dir2                                         
drwxr-xr-x       0       0           0  2025-06-05        259       3  dir1/dir2                                         
drwxr-xr-x       0       0           0  2025-06-05        259       4  dir1/dir2                                         
drwxr-xr-x       0       0           0  2025-06-05        260       0  dir1/dir2/dir3                                    
drwxr-xr-x       0       0           0  2025-06-05        260       1  dir1/dir2/dir3                                    
drwxr-xr-x       0       0           0  2025-06-05        261       0  dir1/dir4                                         
drwxr-xr-x       0       0           0  2025-06-05        261       1  dir1/dir4                                         
drwxr-xr-x       0       0           0  2025-06-05        261       2  dir1/dir4                                         
drwxr-xr-x       0       0           0  2025-06-05        261       3  dir1/dir41                                        
drwxr-xr-x       0       0           0  2025-06-05        261       4  dir1/dir41                                        
drwxr-xr-x       0       0           0  2025-06-05        262       0  dir1/dir4/dir5                                    
drwxr-xr-x       0       0           0  2025-06-05        262       1  dir1/dir4/dir5                                    
drwxr-xr-x       0       0           0  2025-06-05        262       2  dir1/dir2/dir5.moved                              
drwxr-xr-x       0       0           0  2025-06-05        262       3  unlinked                                          
drwxr-xr-x       0       0           0  2025-06-05        262       4  deleted                                           
drwxr-xr-x       0       0           0  2025-06-05        263       0  dir6                                              
drwxr-xr-x       0       0           0  2025-06-05        263       1  dir6                                              
lrwxrwxrwx       0       0           0  2025-06-05        264       0  dir1/dir2/dir3/link1 -> ../../../test1.txt        
prw-r--r--       0       0           0  2025-06-05        265       0  dir1/dir2/named_pipe                              
brw-r--r--       0       0           0  2025-06-05        266       0  dir1/dir2/dir5/block_device                       
brw-r--r--       0       0           0  2025-06-05        266       1  unlinked                                          
brw-r--r--       0       0           0  2025-06-05        266       2  deleted                                           
srwxr-xr-x       0       0           0  2025-06-05        267       0  dir6/aSocket.sock                                 
-rw-r--r--       0       0           5  2025-06-05        268       1  dir1/dir41/test2.txt                              
-rw-r--r--       0       0         445  2025-06-05        269       1  dir1/lorem.txt                                    
-rw-r--r--       0       0         300  2025-06-05        269       2  dir1/lorem.txt                                    
-rw-r--r--       0       0         300  2025-06-05        269       3  dir1/lorem.txt                                    
-rw-r--r--       0       0          10  1970-01-01        513       0  orphan
```

```bash
#> $ python yaffs2_parser.py --image snapshot_12_truncate_lorem_ORPHAN.bin  --autodetect --wide
==> Best format detected : 2048 / 64 in little-endian (score 125)
Processing image snapshot_12_truncate_lorem_ORPHAN.bin with pagesize 2048 and oobsize 64 in little-endian ...

   obj.ID    ver.   parentId  name                                                      mode        size     uid     gid                ctime                atime                mtime    sequence      offset  sha1sum 
      257       1          1  test1.txt                                           -rw-r--r--           5       0       0  2025-06-05 15:25:40  2025-06-05 15:25:40  2025-06-05 15:25:40        4097        2112  b444ac06613fc8d63795be9ad0beaf55011936ac
      258       0          1  dir1                                                drwxr-xr-x           0       0       0  2025-06-05 15:25:45  2025-06-05 15:25:45  2025-06-05 15:25:45        4097        6336  da39a3ee5e6b4b0d3255bfef95601890afd80709
      258       1          1  dir1                                                drwxr-xr-x           0       0       0  2025-06-05 15:25:45  2025-06-05 15:25:45  2025-06-05 15:25:45        4097       23232  da39a3ee5e6b4b0d3255bfef95601890afd80709
      258       2          1  dir1                                                drwxr-xr-x           0       0       0  2025-06-05 15:26:26  2025-06-05 15:25:45  2025-06-05 15:26:26        4097       63360  da39a3ee5e6b4b0d3255bfef95601890afd80709
      258       3          1  dir1                                                drwxr-xr-x           0       0       0  2025-06-05 15:26:38  2025-06-05 15:25:45  2025-06-05 15:26:38        4097       80256  da39a3ee5e6b4b0d3255bfef95601890afd80709
      259       0        258  dir1/dir2                                           drwxr-xr-x           0       0       0  2025-06-05 15:25:45  2025-06-05 15:25:45  2025-06-05 15:25:45        4097        8448  da39a3ee5e6b4b0d3255bfef95601890afd80709
      259       1        258  dir1/dir2                                           drwxr-xr-x           0       0       0  2025-06-05 15:25:45  2025-06-05 15:25:45  2025-06-05 15:25:45        4097       21120  da39a3ee5e6b4b0d3255bfef95601890afd80709
      259       2        258  dir1/dir2                                           drwxr-xr-x           0       0       0  2025-06-05 15:25:57  2025-06-05 15:25:45  2025-06-05 15:25:57        4097       33792  da39a3ee5e6b4b0d3255bfef95601890afd80709
      259       3        258  dir1/dir2                                           drwxr-xr-x           0       0       0  2025-06-05 15:26:14  2025-06-05 15:25:45  2025-06-05 15:26:14        4097       48576  da39a3ee5e6b4b0d3255bfef95601890afd80709
      259       4        258  dir1/dir2                                           drwxr-xr-x           0       0       0  2025-06-05 15:26:20  2025-06-05 15:25:45  2025-06-05 15:26:20        4097       59136  da39a3ee5e6b4b0d3255bfef95601890afd80709
      260       0        259  dir1/dir2/dir3                                      drwxr-xr-x           0       0       0  2025-06-05 15:25:45  2025-06-05 15:25:45  2025-06-05 15:25:45        4097       10560  da39a3ee5e6b4b0d3255bfef95601890afd80709
      260       1        259  dir1/dir2/dir3                                      drwxr-xr-x           0       0       0  2025-06-05 15:25:51  2025-06-05 15:25:45  2025-06-05 15:25:51        4097       29568  da39a3ee5e6b4b0d3255bfef95601890afd80709
      261       0        258  dir1/dir4                                           drwxr-xr-x           0       0       0  2025-06-05 15:25:45  2025-06-05 15:25:45  2025-06-05 15:25:45        4097       12672  da39a3ee5e6b4b0d3255bfef95601890afd80709
      261       1        258  dir1/dir4                                           drwxr-xr-x           0       0       0  2025-06-05 15:25:45  2025-06-05 15:25:45  2025-06-05 15:25:45        4097       19008  da39a3ee5e6b4b0d3255bfef95601890afd80709
      261       2        258  dir1/dir4                                           drwxr-xr-x           0       0       0  2025-06-05 15:26:14  2025-06-05 15:25:45  2025-06-05 15:26:14        4097       46464  da39a3ee5e6b4b0d3255bfef95601890afd80709
      261       3        258  dir1/dir41                                          drwxr-xr-x           0       0       0  2025-06-05 15:26:14  2025-06-05 15:25:45  2025-06-05 15:26:14        4097       61248  da39a3ee5e6b4b0d3255bfef95601890afd80709
      261       4        258  dir1/dir41                                          drwxr-xr-x           0       0       0  2025-06-05 15:26:32  2025-06-05 15:25:45  2025-06-05 15:26:32        4097       71808  da39a3ee5e6b4b0d3255bfef95601890afd80709
      262       0        261  dir1/dir4/dir5                                      drwxr-xr-x           0       0       0  2025-06-05 15:25:45  2025-06-05 15:25:45  2025-06-05 15:25:45        4097       14784  da39a3ee5e6b4b0d3255bfef95601890afd80709
      262       1        261  dir1/dir4/dir5                                      drwxr-xr-x           0       0       0  2025-06-05 15:26:03  2025-06-05 15:25:45  2025-06-05 15:26:03        4097       38016  da39a3ee5e6b4b0d3255bfef95601890afd80709
      262       2        259  dir1/dir2/dir5.moved                                drwxr-xr-x           0       0       0  2025-06-05 15:26:03  2025-06-05 15:25:45  2025-06-05 15:26:03        4097       44352  da39a3ee5e6b4b0d3255bfef95601890afd80709
      262       3          3  unlinked                                            drwxr-xr-x           0       0       0  2025-06-05 15:26:20  2025-06-05 15:25:45  2025-06-05 15:26:20        4097       54912  da39a3ee5e6b4b0d3255bfef95601890afd80709
      262       4          4  deleted                                             drwxr-xr-x           0       0       0  2025-06-05 15:26:20  2025-06-05 15:25:45  2025-06-05 15:26:20        4097       57024  da39a3ee5e6b4b0d3255bfef95601890afd80709
      263       0          1  dir6                                                drwxr-xr-x           0       0       0  2025-06-05 15:25:45  2025-06-05 15:25:45  2025-06-05 15:25:45        4097       16896  da39a3ee5e6b4b0d3255bfef95601890afd80709
      263       1          1  dir6                                                drwxr-xr-x           0       0       0  2025-06-05 15:26:09  2025-06-05 15:25:45  2025-06-05 15:26:09        4097       42240  da39a3ee5e6b4b0d3255bfef95601890afd80709
      264       0        260  dir1/dir2/dir3/link1 -> ../../../test1.txt          lrwxrwxrwx           0       0       0  2025-06-05 15:25:51  2025-06-05 15:25:51  2025-06-05 15:25:51        4097       27456  da39a3ee5e6b4b0d3255bfef95601890afd80709
      265       0        259  dir1/dir2/named_pipe                                prw-r--r--           0       0       0  2025-06-05 15:25:57  2025-06-05 15:25:57  2025-06-05 15:25:57        4097       31680  da39a3ee5e6b4b0d3255bfef95601890afd80709
      266       0        262  dir1/dir2/dir5/block_device                         brw-r--r--           0       0       0  2025-06-05 15:26:03  2025-06-05 15:26:03  2025-06-05 15:26:03        4097       35904  da39a3ee5e6b4b0d3255bfef95601890afd80709
      266       1          3  unlinked                                            brw-r--r--           0       0       0  2025-06-05 15:26:03  2025-06-05 15:26:03  2025-06-05 15:26:03        4097       50688  da39a3ee5e6b4b0d3255bfef95601890afd80709
      266       2          4  deleted                                             brw-r--r--           0       0       0  2025-06-05 15:26:03  2025-06-05 15:26:03  2025-06-05 15:26:03        4097       52800  da39a3ee5e6b4b0d3255bfef95601890afd80709
      267       0        263  dir6/aSocket.sock                                   srwxr-xr-x           0       0       0  2025-06-05 15:26:09  2025-06-05 15:26:09  2025-06-05 15:26:09        4097       40128  da39a3ee5e6b4b0d3255bfef95601890afd80709
      268       1        261  dir1/dir41/test2.txt                                -rw-r--r--           5       0       0  2025-06-05 15:26:32  2025-06-05 15:26:32  2025-06-05 15:26:32        4097       69696  109f4b3c50d7b0df729d299bc6f8e9ef9066971f
      269       1        258  dir1/lorem.txt                                      -rw-r--r--         445       0       0  2025-06-05 15:26:38  2025-06-05 15:26:38  2025-06-05 15:26:38        4097       78144  cd36b370758a259b34845084a6cc38473cb95e27
      269       2        258  dir1/lorem.txt                                      -rw-r--r--         300       0       0  2025-06-05 15:26:43  2025-06-05 15:26:38  2025-06-05 15:26:43        4097       84480  60accecac6e1cc29957ae0b03b8e9033fd08882d
      269       3        258  dir1/lorem.txt                                      -rw-r--r--         300       0       0  2025-06-05 15:26:43  2025-06-05 15:26:38  2025-06-05 15:26:43        4097       86592  60accecac6e1cc29957ae0b03b8e9033fd08882d
      513       0          1  orphan                                              -rw-r--r--          10       0       0  1970-01-01 01:00:01  1970-01-01 01:00:00  1970-01-01 01:00:01        8193    69201792  455bcd5917c990aa6cb6ef04028dbeaac5a176ce
```

All objects listed are restorable (except UNIX socket) : just add --outdir directory

**Note** we can seen/restore every versions even orphan.

An orphan is a file without header informations (no owner/group, size, etc.)


### Launch the test environment

It's a QEMU emulation.

-> go to /test_env directory

## Documentation

A comprehensive explanation of the YAFFS2 file format and how the tool operates is available in the docs/ directory.

Topics include:
- Internal YAFFS2 block structure
- NAND page and OOB layout
- Tool architecture and data flow
- Case studies and analysis examples

## YAFFS2 Snapshots

The samples/ directory contains:
- Raw YAFFS2 partition images (some intentionally corrupted or obfuscated)
- Sample analysis scenarios with accompanying notes or comments

## TODO

- Improved CLI and user interface
- Partial support for YAFFS1
- Enhanced handling of bad blocks and spare areas
- Automatic HTML or JSON reporting

## License

This project is released under the MIT License.

## Contributing

Contributions are welcome!
- Fork this repository
- Create a new branch (git checkout -b feature/my-feature)
- Commit your changes (git commit -am 'Add new feature')
- Push to your fork (git push origin feature/my-feature)
- Open a Pull Request


