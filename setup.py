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
    description='Mistral actions to execute Celery tasks',
    version='1.0.0',
    author='Collabo Team',
    download_url='https://github.com/collabo-br/mistral-celery-actions/archive/1.0.0.tar.gz',
    keywords=['workflow', 'actions', 'mistral', 'celery'],
    install_requires=required
)
