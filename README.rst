robotframework-faker
====================

.. image:: https://travis-ci.org/marketsquare/robotframework-faker.svg?branch=master
    :target: https://pypi.python.org/pypi/robotframework-faker
.. image:: https://img.shields.io/pypi/v/robotframework-faker.svg
    :target: https://pypi.python.org/pypi/robotframework-faker
.. image:: https://img.shields.io/pypi/dm/robotframework-faker.svg
    :target: https://pypi.python.org/pypi/robotframework-faker
.. image:: https://img.shields.io/pypi/l/robotframework-faker.svg
    :target: https://pypi.python.org/pypi/robotframework-faker

Robot Framework keyword library wrapper for
`Faker <https://github.com/joke2k/faker>`__.

This module allows easy use of Faker's random test data generation in
Robot Framework. I hate using static test data, because inevitably the
system under test evolves to pass the tests without necessarily solving
the root cause of bugs.

Any docstrings Faker provides are passed through to Robot Framework, so
they're available in RIDE and in keyword documentation generated via
libdoc.

For more information on Robot Framework please visit `the Robot
Framework homepage! <http://robotframework.org/>`__

Installation
------------

``pip install robotframework-faker``

Faker package dependency
------------------------

Starting with FakerLibrary v6.0.0, the corresponding version of Faker Python package
is no longed pinned in its requirements. It will be up to the users of this library to
select and, if decided upon, to pin the version in their own setup and CI environments.
Note this means the keyword documentation may not match that on the users system.

Usage
-----

`FakerLibrary keyword
documentation <https://marketsquare.github.io/robotframework-faker/>`__

.. code:: robotframework

    *** Settings ***
    Library    FakerLibrary

    *** Test Cases ***
    FakerLibrary Words Generation
        ${words}=    FakerLibrary.Words
        Log    words: ${words}
        ${words}=    FakerLibrary.Words    nb=${10}
        Log    words: ${words}

You can also specify seeds and providers:

.. code:: robotframework

    *** Settings ***
    Library    FakerLibrary    locale=de_DE    seed=124

See `FakerLibrary's tests <https://github.com/marketsquare/robotframework-faker/tree/master/tests/>`__ for more usage examples.

Contribute
----------

If you like this module, please contribute! We welcome patches,
documentation, issues, ideas, and so on.


