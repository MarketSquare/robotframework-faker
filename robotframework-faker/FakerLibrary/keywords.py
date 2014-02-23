import sys

import faker

"""

This is a very thin wrapper for faker. You can access all of faker's usual methods
via FakerLibrary calls in Robot Framework.

"""

# create our faker
_fake = faker.Factory.create()


class FakerKeywords(object):
    ROBOT_LIBRARY_SCOPE = 'Global'


# set all of the faker's public methods to be our methods
for method_name, method in _fake.__dict__.items():
    try:
        if not method_name[0] == '_':
            setattr(sys.modules[__name__].FakerKeywords, method_name, method)
    except (IndexError, AttributeError):
        import traceback
        traceback.print_exc()

