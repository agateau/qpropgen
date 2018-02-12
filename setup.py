#!/usr/bin/env python3
from setuptools import setup

import qpropgen

setup(
    name=qpropgen.__appname__,
    version=qpropgen.__version__,
    description=qpropgen.DESCRIPTION,
    author='Aurélien Gâteau',
    author_email='mail@agateau.com',
    license=qpropgen.__license__,
    platforms=['any'],
    packages=['qpropgen'],
    package_data={
        'qpropgen': ['templates/template.h', 'templates/template.cpp']
    },
    install_requires=['PyYAML', 'jinja2'],
    entry_points={
        'console_scripts': [
            'qpropgen = qpropgen.main:main',
        ],
    },
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Build Tools',
    ]
)
