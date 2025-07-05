#!/usr/bin/env python
from setuptools import setup

short_description = (
    "Robot Framework wrapper for faker, a fake test data generator"
)
try:
    description = open("README.rst").read()
except IOError:
    description = short_description


classifiers = """
Development Status :: 5 - Production/Stable
License :: OSI Approved :: MIT License
Operating System :: OS Independent
Programming Language :: Python
Programming Language :: Python :: 3
Programming Language :: Python :: 3 :: Only
Programming Language :: Python :: 3.9
Programming Language :: Python :: 3.10
Programming Language :: Python :: 3.11
Programming Language :: Python :: 3.12
Programming Language :: Python :: 3.13
Topic :: Software Development :: Testing
Topic :: Software Development :: Quality Assurance
""".strip().splitlines()

setup(
    name="robotframework-faker",
    package_dir={"": "robotframework-faker"},
    packages=["FakerLibrary"],  # this must be the same as the name above
    version="5.0.0",
    description=short_description,
    author="Guy Kisel",
    author_email="guy.kisel@gmail.com",
    url="https://github.com/guykisel/robotframework-faker",
    download_url="https://pypi.python.org/pypi/robotframework-faker",
    keywords=(
        "robotframework testing "
        "test automation testautomation "
        "atdd bdd faker"
    ),  # arbitrary keywords
    install_requires=["faker", "robotframework", "wrapt"],
    long_description=description,
    license="MIT",
    classifiers=classifiers,
    platforms="any",
)
