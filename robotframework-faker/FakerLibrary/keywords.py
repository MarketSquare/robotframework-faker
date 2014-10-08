import faker
import faker.generator

"""

This is a very thin wrapper for faker. You can access all of faker's usual methods
via FakerLibrary calls in Robot Framework.

"""


class FakerKeywords(object):
    """
    This looks tricky but it's just the Robot Framework Hybrid Library API.
    http://robotframework.googlecode.com/hg/doc/userguide/RobotFrameworkUserGuide.html#hybrid-library-api
    """

    ROBOT_LIBRARY_SCOPE = 'Global'
    _fake = faker.Faker()

    def __init__(self, locale=None, providers=None, seed=None):
        self._fake = faker.Faker(locale, providers)
        if seed:
            self._fake.seed(seed)

    def get_keyword_names(self):
        keywords = [name for name, function in self._fake.__dict__.items() if
                    hasattr(function, '__call__')]

        keywords.extend([name for name, function in
                         faker.generator.Generator.__dict__.items() if
                         hasattr(function, '__call__')])
        return keywords

    def __getattr__(self, name):
        func = None
        if name in self._fake.__dict__.keys():
            func = getattr(self._fake, name)
        elif name in faker.generator.Generator.__dict__.keys():
            func = faker.generator.Generator.__dict__[name]
        if func:
            return func
        raise AttributeError('Non-existing keyword "{0}"'.format(name))
