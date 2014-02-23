import faker

"""

This is a very thin wrapper for faker. You can access all of faker's usual methods
via FakerLibrary calls in Robot Framework.

"""


class FakerLibrary(object):

    def __new__(cls, *args, **kwargs):
        # create our faker
        cls._fake = faker.Factory.create(**kwargs)

        # set all of the faker's public methods to be our methods
        for method_name, method in cls._fake.__dict__.items():
            if not method_name[0] == '_':
                setattr(cls, method_name, method)


