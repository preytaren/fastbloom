#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup


NAME = "pybloomfilter"

PACKAGES = ["pybloomfilter", ]

DESCRIPTION = "This is a lightweight but fast bloomfilter."

LONG_DESCRIPTION = ""

KEYWORDS = ("bloomfilter", "hash", "bitset", "python")

AUTHOR = "preyta ren"

AUTHOR_EMAIL = "preyta@163.com"

URL = "https://github.com/preytaren/fastbloom"

VERSION = "v0.1.0"

LICENSE = "MIT"

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=['pyhash>=0.8.1', ],
    keywords=KEYWORDS,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license=LICENSE,
    packages=PACKAGES,
    include_package_data=True,
    zip_safe=True,
)
