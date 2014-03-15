import faker

"""

This is a very thin wrapper for faker. You can access all of faker's usual methods
via FakerLibrary calls in Robot Framework.

"""

# create our faker
_fake = faker.Factory.create()


class FakerKeywords(object):
    ROBOT_LIBRARY_SCOPE = 'Global'

    def __init__(self, locale=None, providers=None):
        global _fake
        _fake = faker.Factory.create(locale, providers)

    def get_keyword_names(self):
        return [name for name, function in _fake.__dict__.items() if hasattr(function, '__call__')]

    def __getattr__(self, name):
        if name in _fake.__dict__:
            return _fake.__dict__[name]
        raise AttributeError('Non-existing keyword "{}"'.format(name))
