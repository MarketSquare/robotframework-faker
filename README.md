robotframework-faker
====================
[![build status](https://travis-ci.org/guykisel/robotframework-faker.svg?branch=master)](https://pypi.python.org/pypi/robotframework-faker)
[![PyPi version](https://pypip.in/v/robotframework-faker/badge.png)](https://pypi.python.org/pypi/robotframework-faker)
[![PyPi downloads](https://pypip.in/d/robotframework-faker/badge.png)](https://pypi.python.org/pypi/robotframework-faker)
[![PyPi downloads](https://pypip.in/license/robotframework-faker/badge.png)](https://pypi.python.org/pypi/robotframework-faker)

Robot Framework keyword library wrapper for [Faker](https://github.com/joke2k/faker).

This module allows easy use of Faker's random test data generation in Robot Framework. I hate using static test data, because inevitably the system under test evolves to pass the tests without necessarily solving the root cause of bugs.

Any docstrings Faker provides are passed through to Robot Framework, so they're available in RIDE and in keyword documentation generated via libdoc.

For more information on Robot Framework please visit [the Robot Framework homepage!](http://robotframework.org/)


Installation
--------------------
`pip install robotframework-faker`

Usage
--------------------
```
*** Settings ***
Library    FakerLibrary

*** Test Cases ***
FakerLibrary Words Generation
    ${words}=    FakerLibrary.Words
    Log    words: ${words}
    ${words}=    FakerLibrary.Words    nb=10
    Log    words: ${words}
```
You can also specify seeds and providers:
```
*** Settings ***
Library    FakerLibrary    locale=de_DE    seed=124
```
See FakerLibrary's tests for more usage examples.

Contribute
--------------------
If you like this module, please contribute! I welcome patches, documentation, issues, ideas, and so on.
