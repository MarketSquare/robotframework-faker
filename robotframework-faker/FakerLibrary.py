import faker

"""

This is a very thin wrapper for faker. You can access all of faker's usual methods
via FakerLibrary calls in Robot Framework.

"""


class FakerLibrary(object):
    def __init__(self, **kwargs):
        # create our faker
        self._fake = faker.Factory.create(**kwargs)

        # set all of the faker's public methods to be our methods
        for method_name, method in self._fake.__dict__.items():
            if not method_name[0] == '_':
                setattr(self, method_name, method)

