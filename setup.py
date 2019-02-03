#!/usr/bin/env python

from distutils.command.build_py import build_py as _build_py
from distutils.core import setup

class 

setup(
        name='infini-study',
        version='0.1',
        description='Practice problem generator and scheduler',
        author='Timothy Morland, Mitchell Ottaway',
        author_email='thetimmorland@gmail.com, mitchello288@gmail.com',
        url='https://github.com/thetimmorland/infini-study',
        packages=['infini-study'],
        install_requires=[
            'jupyter',
            'pyqt5==5.9.2',
        ],
        )

