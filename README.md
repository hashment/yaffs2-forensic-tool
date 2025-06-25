# YAFFS2 Forensic Toolkit

**A forensic analysis tool for YAFFS2 partitions**, enabling extraction, parsing, and inspection of data from embedded systems using the YAFFS2 file system.

## Project Structure

This repository includes:

- `nand.py` – Main program for YAFFS2 parsing and analysis.
- `Yaffs2Forensic.py` – Core Python class implementing YAFFS2 forensic analysis logic.
- `docs/` – Complete documentation on the YAFFS2 file system and analysis methodology.
- `test_env/` – Fully functional test environment featuring:
  - `run.sh` – Script to launch a QEMU virtual machine.
  - `initramfs.cpio.gz` – Initramfs root filesystem used by QEMU.
  - `root_container.img` – EXT2 partition image.
  - `bzImage` – Linux 3.2.0 kernel image.
- `samples/` – YAFFS2 partition snapshots for analysis and experimentation.

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
usage : python nandparser.py [-h] --image IMAGE 	[--obj_ids OBJ_IDS [OBJ_IDS …]]
					[--obj_id_from OBJ_ID_FROM]
					[--obj_id_to OBJ_ID_TO]
					[--snapshot SNAPSHOT]
					[--name NAME]
					[--versions VERSIONS [VERSIONS …]]
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
example :

python nandparser.py --image snapshot_12_truncate_lorem_ORPHAN.bin --wide -outdir /tmp/foo 
```

This will show everything present in the YAFFS2 image and restore as much as possible in /tmp/foo


### Launch the test environment

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


