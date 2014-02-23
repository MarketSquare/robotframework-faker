#!/usr/bin/env python

from distutils.core import setup

from setuptools import find_packages


name = 'Guy Kisel'
address = 'guy.kisel@gmail.com'

setup(name='robotframework-faker',
      version='0.1',
      description='Robot Framework wrapper for faker, a fake test data generator',
      author=name,
      author_email=address,
      url='https://github.com/guykisel/robotframework-faker',
      packages=find_packages(),
      install_requires=['fake-factory', 'robotframework'],
)
