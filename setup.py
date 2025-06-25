from setuptools import setup, find_packages

setup(
    name='yaffs2-forensic',
    version='0.1.0',
    description='YAFFS2 forensic analysis toolkit for NAND flash dumps',
    author='Ton Nom',
    author_email='ton.email@example.com',
    py_modules=['nand', 'Yaffs2Forensic'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Security :: Forensics',
    ],
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'yaffs2tool=nand:main',  # Supposant que tu as une fonction `main()` dans nand.py
        ],
    },
)