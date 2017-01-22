#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='',
    version='0.1',
    author='Alex Ellwein',
    author_email='alex.ellwein@gmail.com',
    url='',
    description='',
    long_description=read('README.md'),
    license='',
    install_requires=[],
    entry_points={
        'console_scripts': []
    }
)
