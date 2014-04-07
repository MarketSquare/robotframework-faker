import faker

"""

This is a very thin wrapper for faker. You can access all of faker's usual methods
via FakerLibrary calls in Robot Framework.

"""

# create our faker
_fake = faker.Factory.create()


class FakerKeywords(object):
    """ 
    This looks tricky but it's just the Robot Framework Hybrid Library API. 
    http://robotframework.googlecode.com/hg/doc/userguide/RobotFrameworkUserGuide.html#hybrid-library-api
    """
    
    ROBOT_LIBRARY_SCOPE = 'Global'

    def __init__(self, locale=None, providers=None, seed=None):
        global _fake
        _fake = faker.Factory.create(locale, providers)
        if seed:
            _fake.seed(seed)

    def get_keyword_names(self):
        keywords = [name for name, function in _fake.__dict__.items() if hasattr(function, '__call__')]
        keywords.append('seed')

    def seed(self, seed_value):
        return _fake.seed(seed_value)

    def __getattr__(self, name):
        if name in _fake.__dict__:
            return _fake.__dict__[name]
        raise AttributeError('Non-existing keyword "{}"'.format(name))
