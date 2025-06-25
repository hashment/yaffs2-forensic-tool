#!/bin/bash
qemu-system-x86_64  \
	-kernel ./bzImage \
        -m 512M \
	-initrd ./initramfs.cpio.gz \
        -drive file=./rootfs_container.img,format=raw,if=virtio \
        -d guest_errors \
        -nographic \
	-serial mon:stdio \
	-append "console=ttyS0 console=/dev/console init=/test.sh"
