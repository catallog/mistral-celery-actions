#!/usr/bin/env python

import os
from setuptools import setup


with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    setup_requires=['pbr'],
    package_dir={'': '.'},
    py_modules=['celery_actions'],
    pbr=True,
    version='1.0.0',
    author='Collabo Team',
    install_requires=required
)
