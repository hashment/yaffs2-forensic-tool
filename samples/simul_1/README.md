# YAFFS2 sample images

This directory contains YAFFS2 images for testing.

## Operating procedure

To generate all of them, in the /test_env, run :

```bash
cd ../test_env
./run.sh

[    0.000000] Initializing cgroup subsys cpuset
[    0.000000] Initializing cgroup subsys cpu
[    0.000000] Linux version 3.2.0 (seb@seb-AE8) (gcc version 4.9.4 (GCC) ) #19 SMP Mon May 26 16:54:16 CEST 2025
[    0.000000] Command line: console=ttyS0 console=/dev/console init=/test.sh
[    0.000000] BIOS-provided physical RAM map:
[    0.000000]  BIOS-e820: 0000000000000000 - 000000000009fc00 (usable)
[    0.000000]  BIOS-e820: 000000000009fc00 - 00000000000a0000 (reserved)
[    0.000000]  BIOS-e820: 00000000000f0000 - 0000000000100000 (reserved)
[    0.000000]  BIOS-e820: 0000000000100000 - 000000001ffdd000 (usable)
[    0.000000]  BIOS-e820: 000000001ffdd000 - 0000000020000000 (reserved)
[    0.000000]  BIOS-e820: 00000000fffc0000 - 0000000100000000 (reserved)
[    0.000000]  BIOS-e820: 000000fd00000000 - 0000010000000000 (reserved)
--[snip]--
[    1.770357] ip6_tables: (C) 2000-2006 Netfilter Core Team
[    1.771312] IPv6 over IPv4 tunneling driver
[    1.772969] NET: Registered protocol family 17
[    1.773279] Registering the dns_resolver key type
[    1.774627] registered taskstats version 1
[    1.776498]   Magic number: 13:843:437
[    1.776887] console [netcon0] enabled
[    1.776990] netconsole: network logging started
[    1.784011] Freeing unused kernel memory: 680k freed
[    1.818814] Write protecting the kernel read-only data: 12288k
[    1.824768] Freeing unused kernel memory: 692k freed
[    1.837486] Freeing unused kernel memory: 1608k freed
====[ Init start ]====
====[ Mdev starting ]====
[    1.916410] Refined TSC clocksource calibration: 3792.848 MHz.
[    1.916628] Switching to clocksource tsc
====[ Mounting ]====
[    1.936878] EXT2-fs (vda): warning: mounting unchecked fs, running e2fsck is recommended
====[ Modifying PATH ]====
====[ Dropping to shell ]====
/bin/sh: can't access tty; job control turned off
~ #
```

When the system is started, there will have a /mnt/disk partition (ext2) mounted.

Then simply run :

```bash
~ # ./simul_1
====[ Erasing flash on /dev/mtd1 ]====
[   37.309787] ====[ Erasing flash on /dev/mtd1 ]====
Erasing 65536 Kibyte @ 0 -- 100 % complete 
====[ Flashing /dev/mtd1 ]====
[   37.330954] ====[ Flashing /dev/mtd1 ]====
Writing data to block 0 at offset 0x0
Writing data to block 1 at offset 0x20000
Writing data to block 2 at offset 0x40000
Writing data to block 3 at offset 0x60000
Writing data to block 4 at offset 0x80000
Writing data to block 5 at offset 0xa0000
Writing data to block 6 at offset 0xc0000
Writing data to block 7 at offset 0xe0000
Writing data to block 8 at offset 0x100000
Writing data to block 9 at offset 0x120000
Writing data to block 10 at offset 0x140000
Writing data to block 11 at offset 0x160000
Writing data to block 12 at offset 0x180000
Writing data to block 13 at offset 0x1a0000
Writing data to block 14 at offset 0x1c0000
Writing data to block 15 at offset 0x1e0000
Writing data to block 16 at offset 0x200000
Writing data to block 17 at offset 0x220000
Writing data to block 18 at offset 0x240000
Writing data to block 19 at offset 0x260000
Writing data to block 20 at offset 0x280000
Writing data to block 21 at offset 0x2a0000
Writing data to block 22 at offset 0x2c0000
Writing data to block 23 at offset 0x2e0000
Writing data to block 24 at offset 0x300000
Writing data to block 25 at offset 0x320000
Writing data to block 26 at offset 0x340000
Writing data to block 27 at offset 0x360000
Writing data to block 28 at offset 0x380000
Writing data to block 29 at offset 0x3a0000
Writing data to block 30 at offset 0x3c0000
Writing data to block 31 at offset 0x3e0000
Writing data to block 32 at offset 0x400000
Writing data to block 33 at offset 0x420000
Writing data to block 34 at offset 0x440000
Writing data to block 35 at offset 0x460000
Writing data to block 36 at offset 0x480000
Writing data to block 37 at offset 0x4a0000
Writing data to block 38 at offset 0x4c0000
Writing data to block 39 at offset 0x4e0000
Writing data to block 40 at offset 0x500000
Writing data to block 41 at offset 0x520000
Writing data to block 42 at offset 0x540000
Writing data to block 43 at offset 0x560000
Writing data to block 44 at offset 0x580000
Writing data to block 45 at offset 0x5a0000
Writing data to block 46 at offset 0x5c0000
Writing data to block 47 at offset 0x5e0000
Writing data to block 48 at offset 0x600000
Writing data to block 49 at offset 0x620000
Writing data to block 50 at offset 0x640000
Writing data to block 51 at offset 0x660000
Writing data to block 52 at offset 0x680000
Writing data to block 53 at offset 0x6a0000
Writing data to block 54 at offset 0x6c0000
Writing data to block 55 at offset 0x6e0000
Writing data to block 56 at offset 0x700000
Writing data to block 57 at offset 0x720000
Writing data to block 58 at offset 0x740000
Writing data to block 59 at offset 0x760000
Writing data to block 60 at offset 0x780000
Writing data to block 61 at offset 0x7a0000
Writing data to block 62 at offset 0x7c0000
Writing data to block 63 at offset 0x7e0000
Writing data to block 64 at offset 0x800000
Writing data to block 65 at offset 0x820000
Writing data to block 66 at offset 0x840000
Writing data to block 67 at offset 0x860000
Writing data to block 68 at offset 0x880000
Writing data to block 69 at offset 0x8a0000
Writing data to block 70 at offset 0x8c0000
Writing data to block 71 at offset 0x8e0000
Writing data to block 72 at offset 0x900000
Writing data to block 73 at offset 0x920000
Writing data to block 74 at offset 0x940000
Writing data to block 75 at offset 0x960000
Writing data to block 76 at offset 0x980000
Writing data to block 77 at offset 0x9a0000
Writing data to block 78 at offset 0x9c0000
Writing data to block 79 at offset 0x9e0000
Writing data to block 80 at offset 0xa00000
Writing data to block 81 at offset 0xa20000
Writing data to block 82 at offset 0xa40000
Writing data to block 83 at offset 0xa60000
Writing data to block 84 at offset 0xa80000
Writing data to block 85 at offset 0xaa0000
Writing data to block 86 at offset 0xac0000
Writing data to block 87 at offset 0xae0000
Writing data to block 88 at offset 0xb00000
Writing data to block 89 at offset 0xb20000
Writing data to block 90 at offset 0xb40000
Writing data to block 91 at offset 0xb60000
Writing data to block 92 at offset 0xb80000
Writing data to block 93 at offset 0xba0000
Writing data to block 94 at offset 0xbc0000
Writing data to block 95 at offset 0xbe0000
Writing data to block 96 at offset 0xc00000
Writing data to block 97 at offset 0xc20000
Writing data to block 98 at offset 0xc40000
Writing data to block 99 at offset 0xc60000
Writing data to block 100 at offset 0xc80000
Writing data to block 101 at offset 0xca0000
Writing data to block 102 at offset 0xcc0000
Writing data to block 103 at offset 0xce0000
Writing data to block 104 at offset 0xd00000
Writing data to block 105 at offset 0xd20000
Writing data to block 106 at offset 0xd40000
Writing data to block 107 at offset 0xd60000
Writing data to block 108 at offset 0xd80000
Writing data to block 109 at offset 0xda0000
Writing data to block 110 at offset 0xdc0000
Writing data to block 111 at offset 0xde0000
Writing data to block 112 at offset 0xe00000
Writing data to block 113 at offset 0xe20000
Writing data to block 114 at offset 0xe40000
Writing data to block 115 at offset 0xe60000
Writing data to block 116 at offset 0xe80000
Writing data to block 117 at offset 0xea0000
Writing data to block 118 at offset 0xec0000
Writing data to block 119 at offset 0xee0000
Writing data to block 120 at offset 0xf00000
Writing data to block 121 at offset 0xf20000
Writing data to block 122 at offset 0xf40000
Writing data to block 123 at offset 0xf60000
Writing data to block 124 at offset 0xf80000
Writing data to block 125 at offset 0xfa0000
Writing data to block 126 at offset 0xfc0000
Writing data to block 127 at offset 0xfe0000
Writing data to block 128 at offset 0x1000000
Writing data to block 129 at offset 0x1020000
Writing data to block 130 at offset 0x1040000
Writing data to block 131 at offset 0x1060000
Writing data to block 132 at offset 0x1080000
Writing data to block 133 at offset 0x10a0000
Writing data to block 134 at offset 0x10c0000
Writing data to block 135 at offset 0x10e0000
Writing data to block 136 at offset 0x1100000
Writing data to block 137 at offset 0x1120000
Writing data to block 138 at offset 0x1140000
Writing data to block 139 at offset 0x1160000
Writing data to block 140 at offset 0x1180000
Writing data to block 141 at offset 0x11a0000
Writing data to block 142 at offset 0x11c0000
Writing data to block 143 at offset 0x11e0000
Writing data to block 144 at offset 0x1200000
Writing data to block 145 at offset 0x1220000
Writing data to block 146 at offset 0x1240000
Writing data to block 147 at offset 0x1260000
Writing data to block 148 at offset 0x1280000
Writing data to block 149 at offset 0x12a0000
Writing data to block 150 at offset 0x12c0000
Writing data to block 151 at offset 0x12e0000
Writing data to block 152 at offset 0x1300000
Writing data to block 153 at offset 0x1320000
Writing data to block 154 at offset 0x1340000
Writing data to block 155 at offset 0x1360000
Writing data to block 156 at offset 0x1380000
Writing data to block 157 at offset 0x13a0000
Writing data to block 158 at offset 0x13c0000
Writing data to block 159 at offset 0x13e0000
Writing data to block 160 at offset 0x1400000
Writing data to block 161 at offset 0x1420000
Writing data to block 162 at offset 0x1440000
Writing data to block 163 at offset 0x1460000
Writing data to block 164 at offset 0x1480000
Writing data to block 165 at offset 0x14a0000
Writing data to block 166 at offset 0x14c0000
Writing data to block 167 at offset 0x14e0000
Writing data to block 168 at offset 0x1500000
Writing data to block 169 at offset 0x1520000
Writing data to block 170 at offset 0x1540000
Writing data to block 171 at offset 0x1560000
Writing data to block 172 at offset 0x1580000
Writing data to block 173 at offset 0x15a0000
Writing data to block 174 at offset 0x15c0000
Writing data to block 175 at offset 0x15e0000
Writing data to block 176 at offset 0x1600000
Writing data to block 177 at offset 0x1620000
Writing data to block 178 at offset 0x1640000
Writing data to block 179 at offset 0x1660000
Writing data to block 180 at offset 0x1680000
Writing data to block 181 at offset 0x16a0000
Writing data to block 182 at offset 0x16c0000
Writing data to block 183 at offset 0x16e0000
Writing data to block 184 at offset 0x1700000
Writing data to block 185 at offset 0x1720000
Writing data to block 186 at offset 0x1740000
Writing data to block 187 at offset 0x1760000
Writing data to block 188 at offset 0x1780000
Writing data to block 189 at offset 0x17a0000
Writing data to block 190 at offset 0x17c0000
Writing data to block 191 at offset 0x17e0000
Writing data to block 192 at offset 0x1800000
Writing data to block 193 at offset 0x1820000
Writing data to block 194 at offset 0x1840000
Writing data to block 195 at offset 0x1860000
Writing data to block 196 at offset 0x1880000
Writing data to block 197 at offset 0x18a0000
Writing data to block 198 at offset 0x18c0000
Writing data to block 199 at offset 0x18e0000
Writing data to block 200 at offset 0x1900000
Writing data to block 201 at offset 0x1920000
Writing data to block 202 at offset 0x1940000
Writing data to block 203 at offset 0x1960000
Writing data to block 204 at offset 0x1980000
Writing data to block 205 at offset 0x19a0000
Writing data to block 206 at offset 0x19c0000
Writing data to block 207 at offset 0x19e0000
Writing data to block 208 at offset 0x1a00000
Writing data to block 209 at offset 0x1a20000
Writing data to block 210 at offset 0x1a40000
Writing data to block 211 at offset 0x1a60000
Writing data to block 212 at offset 0x1a80000
Writing data to block 213 at offset 0x1aa0000
Writing data to block 214 at offset 0x1ac0000
Writing data to block 215 at offset 0x1ae0000
Writing data to block 216 at offset 0x1b00000
Writing data to block 217 at offset 0x1b20000
Writing data to block 218 at offset 0x1b40000
Writing data to block 219 at offset 0x1b60000
Writing data to block 220 at offset 0x1b80000
Writing data to block 221 at offset 0x1ba0000
Writing data to block 222 at offset 0x1bc0000
Writing data to block 223 at offset 0x1be0000
Writing data to block 224 at offset 0x1c00000
Writing data to block 225 at offset 0x1c20000
Writing data to block 226 at offset 0x1c40000
Writing data to block 227 at offset 0x1c60000
Writing data to block 228 at offset 0x1c80000
Writing data to block 229 at offset 0x1ca0000
Writing data to block 230 at offset 0x1cc0000
Writing data to block 231 at offset 0x1ce0000
Writing data to block 232 at offset 0x1d00000
Writing data to block 233 at offset 0x1d20000
Writing data to block 234 at offset 0x1d40000
Writing data to block 235 at offset 0x1d60000
Writing data to block 236 at offset 0x1d80000
Writing data to block 237 at offset 0x1da0000
Writing data to block 238 at offset 0x1dc0000
Writing data to block 239 at offset 0x1de0000
Writing data to block 240 at offset 0x1e00000
Writing data to block 241 at offset 0x1e20000
Writing data to block 242 at offset 0x1e40000
Writing data to block 243 at offset 0x1e60000
Writing data to block 244 at offset 0x1e80000
Writing data to block 245 at offset 0x1ea0000
Writing data to block 246 at offset 0x1ec0000
Writing data to block 247 at offset 0x1ee0000
Writing data to block 248 at offset 0x1f00000
Writing data to block 249 at offset 0x1f20000
Writing data to block 250 at offset 0x1f40000
Writing data to block 251 at offset 0x1f60000
Writing data to block 252 at offset 0x1f80000
Writing data to block 253 at offset 0x1fa0000
Writing data to block 254 at offset 0x1fc0000
Writing data to block 255 at offset 0x1fe0000
Writing data to block 256 at offset 0x2000000
Writing data to block 257 at offset 0x2020000
Writing data to block 258 at offset 0x2040000
Writing data to block 259 at offset 0x2060000
Writing data to block 260 at offset 0x2080000
Writing data to block 261 at offset 0x20a0000
Writing data to block 262 at offset 0x20c0000
Writing data to block 263 at offset 0x20e0000
Writing data to block 264 at offset 0x2100000
Writing data to block 265 at offset 0x2120000
Writing data to block 266 at offset 0x2140000
Writing data to block 267 at offset 0x2160000
Writing data to block 268 at offset 0x2180000
Writing data to block 269 at offset 0x21a0000
Writing data to block 270 at offset 0x21c0000
Writing data to block 271 at offset 0x21e0000
Writing data to block 272 at offset 0x2200000
Writing data to block 273 at offset 0x2220000
Writing data to block 274 at offset 0x2240000
Writing data to block 275 at offset 0x2260000
Writing data to block 276 at offset 0x2280000
Writing data to block 277 at offset 0x22a0000
Writing data to block 278 at offset 0x22c0000
Writing data to block 279 at offset 0x22e0000
Writing data to block 280 at offset 0x2300000
Writing data to block 281 at offset 0x2320000
Writing data to block 282 at offset 0x2340000
Writing data to block 283 at offset 0x2360000
Writing data to block 284 at offset 0x2380000
Writing data to block 285 at offset 0x23a0000
Writing data to block 286 at offset 0x23c0000
Writing data to block 287 at offset 0x23e0000
Writing data to block 288 at offset 0x2400000
Writing data to block 289 at offset 0x2420000
Writing data to block 290 at offset 0x2440000
Writing data to block 291 at offset 0x2460000
Writing data to block 292 at offset 0x2480000
Writing data to block 293 at offset 0x24a0000
Writing data to block 294 at offset 0x24c0000
Writing data to block 295 at offset 0x24e0000
Writing data to block 296 at offset 0x2500000
Writing data to block 297 at offset 0x2520000
Writing data to block 298 at offset 0x2540000
Writing data to block 299 at offset 0x2560000
Writing data to block 300 at offset 0x2580000
Writing data to block 301 at offset 0x25a0000
Writing data to block 302 at offset 0x25c0000
Writing data to block 303 at offset 0x25e0000
Writing data to block 304 at offset 0x2600000
Writing data to block 305 at offset 0x2620000
Writing data to block 306 at offset 0x2640000
Writing data to block 307 at offset 0x2660000
Writing data to block 308 at offset 0x2680000
Writing data to block 309 at offset 0x26a0000
Writing data to block 310 at offset 0x26c0000
Writing data to block 311 at offset 0x26e0000
Writing data to block 312 at offset 0x2700000
Writing data to block 313 at offset 0x2720000
Writing data to block 314 at offset 0x2740000
Writing data to block 315 at offset 0x2760000
Writing data to block 316 at offset 0x2780000
Writing data to block 317 at offset 0x27a0000
Writing data to block 318 at offset 0x27c0000
Writing data to block 319 at offset 0x27e0000
Writing data to block 320 at offset 0x2800000
Writing data to block 321 at offset 0x2820000
Writing data to block 322 at offset 0x2840000
Writing data to block 323 at offset 0x2860000
Writing data to block 324 at offset 0x2880000
Writing data to block 325 at offset 0x28a0000
Writing data to block 326 at offset 0x28c0000
Writing data to block 327 at offset 0x28e0000
Writing data to block 328 at offset 0x2900000
Writing data to block 329 at offset 0x2920000
Writing data to block 330 at offset 0x2940000
Writing data to block 331 at offset 0x2960000
Writing data to block 332 at offset 0x2980000
Writing data to block 333 at offset 0x29a0000
Writing data to block 334 at offset 0x29c0000
Writing data to block 335 at offset 0x29e0000
Writing data to block 336 at offset 0x2a00000
Writing data to block 337 at offset 0x2a20000
Writing data to block 338 at offset 0x2a40000
Writing data to block 339 at offset 0x2a60000
Writing data to block 340 at offset 0x2a80000
Writing data to block 341 at offset 0x2aa0000
Writing data to block 342 at offset 0x2ac0000
Writing data to block 343 at offset 0x2ae0000
Writing data to block 344 at offset 0x2b00000
Writing data to block 345 at offset 0x2b20000
Writing data to block 346 at offset 0x2b40000
Writing data to block 347 at offset 0x2b60000
Writing data to block 348 at offset 0x2b80000
Writing data to block 349 at offset 0x2ba0000
Writing data to block 350 at offset 0x2bc0000
Writing data to block 351 at offset 0x2be0000
Writing data to block 352 at offset 0x2c00000
Writing data to block 353 at offset 0x2c20000
Writing data to block 354 at offset 0x2c40000
Writing data to block 355 at offset 0x2c60000
Writing data to block 356 at offset 0x2c80000
Writing data to block 357 at offset 0x2ca0000
Writing data to block 358 at offset 0x2cc0000
Writing data to block 359 at offset 0x2ce0000
Writing data to block 360 at offset 0x2d00000
Writing data to block 361 at offset 0x2d20000
Writing data to block 362 at offset 0x2d40000
Writing data to block 363 at offset 0x2d60000
Writing data to block 364 at offset 0x2d80000
Writing data to block 365 at offset 0x2da0000
Writing data to block 366 at offset 0x2dc0000
Writing data to block 367 at offset 0x2de0000
Writing data to block 368 at offset 0x2e00000
Writing data to block 369 at offset 0x2e20000
Writing data to block 370 at offset 0x2e40000
Writing data to block 371 at offset 0x2e60000
Writing data to block 372 at offset 0x2e80000
Writing data to block 373 at offset 0x2ea0000
Writing data to block 374 at offset 0x2ec0000
Writing data to block 375 at offset 0x2ee0000
Writing data to block 376 at offset 0x2f00000
Writing data to block 377 at offset 0x2f20000
Writing data to block 378 at offset 0x2f40000
Writing data to block 379 at offset 0x2f60000
Writing data to block 380 at offset 0x2f80000
Writing data to block 381 at offset 0x2fa0000
Writing data to block 382 at offset 0x2fc0000
Writing data to block 383 at offset 0x2fe0000
Writing data to block 384 at offset 0x3000000
Writing data to block 385 at offset 0x3020000
Writing data to block 386 at offset 0x3040000
Writing data to block 387 at offset 0x3060000
Writing data to block 388 at offset 0x3080000
Writing data to block 389 at offset 0x30a0000
Writing data to block 390 at offset 0x30c0000
Writing data to block 391 at offset 0x30e0000
Writing data to block 392 at offset 0x3100000
Writing data to block 393 at offset 0x3120000
Writing data to block 394 at offset 0x3140000
Writing data to block 395 at offset 0x3160000
Writing data to block 396 at offset 0x3180000
Writing data to block 397 at offset 0x31a0000
Writing data to block 398 at offset 0x31c0000
Writing data to block 399 at offset 0x31e0000
Writing data to block 400 at offset 0x3200000
Writing data to block 401 at offset 0x3220000
Writing data to block 402 at offset 0x3240000
Writing data to block 403 at offset 0x3260000
Writing data to block 404 at offset 0x3280000
Writing data to block 405 at offset 0x32a0000
Writing data to block 406 at offset 0x32c0000
Writing data to block 407 at offset 0x32e0000
Writing data to block 408 at offset 0x3300000
Writing data to block 409 at offset 0x3320000
Writing data to block 410 at offset 0x3340000
Writing data to block 411 at offset 0x3360000
Writing data to block 412 at offset 0x3380000
Writing data to block 413 at offset 0x33a0000
Writing data to block 414 at offset 0x33c0000
Writing data to block 415 at offset 0x33e0000
Writing data to block 416 at offset 0x3400000
Writing data to block 417 at offset 0x3420000
Writing data to block 418 at offset 0x3440000
Writing data to block 419 at offset 0x3460000
Writing data to block 420 at offset 0x3480000
Writing data to block 421 at offset 0x34a0000
Writing data to block 422 at offset 0x34c0000
Writing data to block 423 at offset 0x34e0000
Writing data to block 424 at offset 0x3500000
Writing data to block 425 at offset 0x3520000
Writing data to block 426 at offset 0x3540000
Writing data to block 427 at offset 0x3560000
Writing data to block 428 at offset 0x3580000
Writing data to block 429 at offset 0x35a0000
Writing data to block 430 at offset 0x35c0000
Writing data to block 431 at offset 0x35e0000
Writing data to block 432 at offset 0x3600000
Writing data to block 433 at offset 0x3620000
Writing data to block 434 at offset 0x3640000
Writing data to block 435 at offset 0x3660000
Writing data to block 436 at offset 0x3680000
Writing data to block 437 at offset 0x36a0000
Writing data to block 438 at offset 0x36c0000
Writing data to block 439 at offset 0x36e0000
Writing data to block 440 at offset 0x3700000
Writing data to block 441 at offset 0x3720000
Writing data to block 442 at offset 0x3740000
Writing data to block 443 at offset 0x3760000
Writing data to block 444 at offset 0x3780000
Writing data to block 445 at offset 0x37a0000
Writing data to block 446 at offset 0x37c0000
Writing data to block 447 at offset 0x37e0000
Writing data to block 448 at offset 0x3800000
Writing data to block 449 at offset 0x3820000
Writing data to block 450 at offset 0x3840000
Writing data to block 451 at offset 0x3860000
Writing data to block 452 at offset 0x3880000
Writing data to block 453 at offset 0x38a0000
Writing data to block 454 at offset 0x38c0000
Writing data to block 455 at offset 0x38e0000
Writing data to block 456 at offset 0x3900000
Writing data to block 457 at offset 0x3920000
Writing data to block 458 at offset 0x3940000
Writing data to block 459 at offset 0x3960000
Writing data to block 460 at offset 0x3980000
Writing data to block 461 at offset 0x39a0000
Writing data to block 462 at offset 0x39c0000
Writing data to block 463 at offset 0x39e0000
Writing data to block 464 at offset 0x3a00000
Writing data to block 465 at offset 0x3a20000
Writing data to block 466 at offset 0x3a40000
Writing data to block 467 at offset 0x3a60000
Writing data to block 468 at offset 0x3a80000
Writing data to block 469 at offset 0x3aa0000
Writing data to block 470 at offset 0x3ac0000
Writing data to block 471 at offset 0x3ae0000
Writing data to block 472 at offset 0x3b00000
Writing data to block 473 at offset 0x3b20000
Writing data to block 474 at offset 0x3b40000
Writing data to block 475 at offset 0x3b60000
Writing data to block 476 at offset 0x3b80000
Writing data to block 477 at offset 0x3ba0000
Writing data to block 478 at offset 0x3bc0000
Writing data to block 479 at offset 0x3be0000
Writing data to block 480 at offset 0x3c00000
Writing data to block 481 at offset 0x3c20000
Writing data to block 482 at offset 0x3c40000
Writing data to block 483 at offset 0x3c60000
Writing data to block 484 at offset 0x3c80000
Writing data to block 485 at offset 0x3ca0000
Writing data to block 486 at offset 0x3cc0000
Writing data to block 487 at offset 0x3ce0000
Writing data to block 488 at offset 0x3d00000
Writing data to block 489 at offset 0x3d20000
Writing data to block 490 at offset 0x3d40000
Writing data to block 491 at offset 0x3d60000
Writing data to block 492 at offset 0x3d80000
Writing data to block 493 at offset 0x3da0000
Writing data to block 494 at offset 0x3dc0000
Writing data to block 495 at offset 0x3de0000
Writing data to block 496 at offset 0x3e00000
Writing data to block 497 at offset 0x3e20000
Writing data to block 498 at offset 0x3e40000
Writing data to block 499 at offset 0x3e60000
Writing data to block 500 at offset 0x3e80000
Writing data to block 501 at offset 0x3ea0000
Writing data to block 502 at offset 0x3ec0000
Writing data to block 503 at offset 0x3ee0000
Writing data to block 504 at offset 0x3f00000
Writing data to block 505 at offset 0x3f20000
Writing data to block 506 at offset 0x3f40000
Writing data to block 507 at offset 0x3f60000
Writing data to block 508 at offset 0x3f80000
Writing data to block 509 at offset 0x3fa0000
Writing data to block 510 at offset 0x3fc0000
Writing data to block 511 at offset 0x3fe0000
Written 32768 blocks containing only 0xff bytes
Those block may be incorrectly treated as empty!
====[ Mounting /dev/mtdblock1 on /mnt/yaffs ]====
[   39.686733] ====[ Mounting /dev/mtdblock1 on /mnt/yaffs ]====
[   39.688538] yaffs: dev is 32505857 name is "mtdblock1" rw
[   39.688687] yaffs: passed flags ""
====[ Dumping initial / on /dev/mtd1 ]====
[   39.694917] ====[ Dumping initial / on /dev/mtd1 ]====
ECC failed: 0
ECC corrected: 0
Number of bad blocks: 0
Number of bbt blocks: 0
Block size 131072, page size 2048, OOB size 64
Dumping data starting at 0x00000000 and ending at 0x04000000...
====[ Creating /mnt/yaffs/file1.txt ]====
[   41.517285] ====[ Creating /mnt/yaffs/file1.txt ]====
ECC failed: 0
ECC corrected: 0
Number of bad blocks: 0
Number of bbt blocks: 0
Block size 131072, page size 2048, OOB size 64
Dumping data starting at 0x00000000 and ending at 0x04000000...
====[ Creating chained directories /mnt/yaffs/dir1/dir2/dir3 ]====
[   48.250692] ====[ Creating chained directories /mnt/yaffs/dir1/dir2/dir3 ]====
====[ Creating chained directories /mnt/yaffs/dir1/dir4/dir5 ]====
[   48.261146] ====[ Creating chained directories /mnt/yaffs/dir1/dir4/dir5 ]====
====[ Creating chained directories /mnt/yaffs/dir6 ]====
[   48.268315] ====[ Creating chained directories /mnt/yaffs/dir6 ]====
ECC failed: 0
ECC corrected: 0
Number of bad blocks: 0
Number of bbt blocks: 0
Block size 131072, page size 2048, OOB size 64
Dumping data starting at 0x00000000 and ending at 0x04000000...
====[ Creating /mnt/yaffs/dir1/dir2/dir3/link1 -> ../../../test1.txt ]====
[   54.999888] ====[ Creating /mnt/yaffs/dir1/dir2/dir3/link1 -> ../../../test1.txt ]====
ECC failed: 0
ECC corrected: 0
Number of bad blocks: 0
Number of bbt blocks: 0
Block size 131072, page size 2048, OOB size 64
Dumping data starting at 0x00000000 and ending at 0x04000000...
====[ Creating named pipe /mnt/yaffs/dir1/dir2/named_pipe ]====
[   61.743501] ====[ Creating named pipe /mnt/yaffs/dir1/dir2/named_pipe ]====
ECC failed: 0
ECC corrected: 0
Number of bad blocks: 0
Number of bbt blocks: 0
Block size 131072, page size 2048, OOB size 64
Dumping data starting at 0x00000000 and ending at 0x04000000...
====[ Creating block device /mnt/yaffs/dir1/dir4/dir5/block_device ]====
[   68.488485] ====[ Creating block device /mnt/yaffs/dir1/dir4/dir5/block_device ]====
ECC failed: 0
ECC corrected: 0
Number of bad blocks: 0
Number of bbt blocks: 0
Block size 131072, page size 2048, OOB size 64
Dumping data starting at 0x00000000 and ending at 0x04000000...
====[ Creating unix socket /mnt/yaffs/dir6/aSocket.sock ]====
[   75.240688] ====[ Creating unix socket /mnt/yaffs/dir6/aSocket.sock ]====
ECC failed: 0
ECC corrected: 0
Number of bad blocks: 0
Number of bbt blocks: 0
Block size 131072, page size 2048, OOB size 64
Dumping data starting at 0x00000000 and ending at 0x04000000...
====[ Moving directory /mnt/yaffs/dir1/dir4/dir5 in /mnt/yaffs/dir1/dir2 ]====
[   81.977201] ====[ Moving directory /mnt/yaffs/dir1/dir4/dir5 in /mnt/yaffs/dir1/dir2 ]====
ECC failed: 0
ECC corrected: 0
Number of bad blocks: 0
Number of bbt blocks: 0
Block size 131072, page size 2048, OOB size 64
Dumping data starting at 0x00000000 and ending at 0x04000000...
====[ Delete /mnt/yaffs/dir1/dir2/dir5 ]====
[   88.714167] ====[ Delete /mnt/yaffs/dir1/dir2/dir5 ]====
ECC failed: 0
ECC corrected: 0
Number of bad blocks: 0
Number of bbt blocks: 0
Block size 131072, page size 2048, OOB size 64
Dumping data starting at 0x00000000 and ending at 0x04000000...
====[ Rename /mnt/yaffs/dir1/dir4 in /mnt/yaffs/dir1/dir41 ]====
[   95.453234] ====[ Rename /mnt/yaffs/dir1/dir4 in /mnt/yaffs/dir1/dir41 ]====
ECC failed: 0
ECC corrected: 0
Number of bad blocks: 0
Number of bbt blocks: 0
Block size 131072, page size 2048, OOB size 64
Dumping data starting at 0x00000000 and ending at 0x04000000...
====[ Creating /mnt/yaffs/dir1/dir41/file2.txt ]====
[  102.215981] ====[ Creating /mnt/yaffs/dir1/dir41/file2.txt ]====
ECC failed: 0
ECC corrected: 0
Number of bad blocks: 0
Number of bbt blocks: 0
Block size 131072, page size 2048, OOB size 64
Dumping data starting at 0x00000000 and ending at 0x04000000...
====[ Copying /mnt/yaffs/dir1/lorem.txt ]====
[  108.938022] ====[ Copying /mnt/yaffs/dir1/lorem.txt ]====
ECC failed: 0
ECC corrected: 0
Number of bad blocks: 0
Number of bbt blocks: 0
Block size 131072, page size 2048, OOB size 64
Dumping data starting at 0x00000000 and ending at 0x04000000...
====[ Truncating /mnt/yaffs/dir1/lorem.txt ]====
[  115.669385] ====[ Truncating /mnt/yaffs/dir1/lorem.txt ]====
ECC failed: 0
ECC corrected: 0
Number of bad blocks: 0
Number of bbt blocks: 0
Block size 131072, page size 2048, OOB size 64
Dumping data starting at 0x00000000 and ending at 0x04000000...
====[ Fin ]====
[  122.403254] ====[ Fin ]====

```

All snapshots are saved in /mnt/disk/result/simul_1

Then exit the QEMU emulation with 

```bash
~ # halt -f
```

# Explore Snapshot

First of all you need to mount ext2 partition named rootfs_container.img with command :

```bash
#> mkdir -p recup
#> sudo mount -t ext2 -o loop  rootfs_container.img  recup/
```

In recup directory, there will be :
-recup
  - snapshot_00_empty.bin.gz
  - files_in_fs
  - result
    - simul_1
      - snapshot_00_empty.bin.gz
      - snapshot_01_add_test1.bin.gz
      - snapshot_02_creat_directories.bin.gz
      - snapshot_03_creat_link1.bin.gz
      - snapshot_04_create_named_pipe.bin.gz
      - snapshot_05_creat_block_device.bin.gz
      - snapshot_06_creat_unix_socket.bin.gz
      - snapshot_07_move_dir5_dir2.bin.gz
      - snapshot_08_delete_dir2dir5.bin.gz
      - snapshot_09_rename_dir4.bin.gz
      - snapshot_10_add_test2.bin.gz
      - snapshot_11_add_lorem.bin.gz
      - snapshot_12_truncate_lorem.bin.gz
      - snapshot_13_truncate_lorem_ORPHAN.bin.gz

If you want to explore one of them, *do not forget* to unzip it first before running nand.py tools.
