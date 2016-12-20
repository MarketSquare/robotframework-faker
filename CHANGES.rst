Changelog for robotframework-faker
===========================

4.0.0 (2016-12-19)
------------------

- fake-factory was renamed to faker. (thanks @funkymonkeymonk)
- Dropped Python 2.6 support since faker no longer supports it. (thanks @funkymonkeymonk)


3.0.0 (2015-02-05)
------------------

- Use robotframework syntax highlighting in README.rst examples.
  (thanks @pekkaklarck)
- Autocast string inputs to their most likely types. Adds wrapt as a dependency.
  NOTE: This change breaks some backwards-compatibility.
- Set up static analysis in Travis-CI.


2.0.4 (2014-10-09)
------------------

- Remove changelog from PyPI long_description, it breaks the rst rendering :(


2.0.3 (2014-10-09)
------------------

- Fixed example in README.
- Add changelog to PyPI long_description.


2.0.2 (2014-10-09)
------------------

- Hotfix: Fix README.rst for PyPI compatibility.


2.0.1 (2014-10-09)
------------------

- Hotfix: Deleted invalid classifier.


2.0.0 (2014-10-09)
------------------

- Removed autocasting of input variables. This change is backwards
  incompatible! Going forward, to input non-string data types to FakerLibrary
  keywords, you must format them using RF's syntax for those data types.
  For example, the integer 3 would be ${3}.
- Began using zest.releaser for automated packaging and releasing.
- Added pre-commit configuration to ensure PEP-8 compliance.
- Switched README to restructuredtext to improve rendering on PyPI.
