Changelog for robotframework-faker
===========================

2.0.2 (unreleased)
------------------

- Nothing changed yet.


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
