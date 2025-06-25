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

Install required packages with:

```bash
pip install -r requirements.txt
```

## Usage

### Analyze a YAFFS2 partition dump

```bash
python nand.py -i dump.yaffs2 -o output_dir
```

### Launch the test environment

```bash
cd test_env
./run.sh
```
This will boot a QEMU virtual machine simulating an embedded Linux system with a YAFFS2 NAND partition, allowing realistic file creation and extraction testing.

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


