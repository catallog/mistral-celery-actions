#!/usr/bin/env python

from setuptools import setup


setup(
    setup_requires=['pbr'],
    package_dir={'': '.'},
    py_modules=['celery_actions'],
    pbr=True,
)
