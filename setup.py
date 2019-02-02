#!/usr/bin/env python

from distutils.core import setup

setup(
        name='infini-study',
        version='0.1',
        description='Practice problem generator and scheduler',
        author='Timothy Morland',
        author_email='thetimmorland@gmail.com',
        url='https://github.com/thetimmorland/infini-study',
        packages=['infini-study'],
        install_requires=[
            'jupyter',
        ],
        )

