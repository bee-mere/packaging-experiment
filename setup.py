#!/usr/bin/env python

from distutils.core import setup

setup(
    name='hello-pack',
    version='0.1dev',
    packages=['hi-package'],
    entry_points = {
        'console_scripts': [
            'hi-pack-sayhi=hi-package:main'
        ]
    }
)
