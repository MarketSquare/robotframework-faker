#!/usr/bin/env python

from distutils.core import setup

short_description = 'Robot Framework wrapper for faker, a fake test data generator'
try:
    description = open('README.md').read()
except IOError:
    description = short_description

try:
    license = open('LICENSE').read()
except IOError:
    license = 'MIT License'

setup(
    name='robotframework-faker',
    package_dir={'': 'robotframework-faker'},
    packages=['FakerLibrary'],  # this must be the same as the name above
    version='0.6',
    description=short_description,
    author='Guy Kisel',
    author_email='guy.kisel@gmail.com',
    url='https://github.com/guykisel/robotframework-faker',
    keywords='robotframework testing test automation faker',  # arbitrary keywords
    classifiers=[],
    install_requires=['fake-factory', 'robotframework'],
    long_description=description,
    license=license,
)
