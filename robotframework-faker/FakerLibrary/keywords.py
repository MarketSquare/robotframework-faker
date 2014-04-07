import faker
import faker.generator

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
        keywords.extend(
            [name for name, function in faker.generator.Generator.__dict__.items() if
             hasattr(function, '__call__')])

    def __getattr__(self, name):
        if name in _fake.__dict__.keys():
            return _autocast(_fake.__dict__[name])
        elif name in faker.generator.Generator.__dict__.keys():
            return _autocast(faker.generator.Generator.__dict__[name])
        raise AttributeError('Non-existing keyword "{}"'.format(name))


#
# From https://stackoverflow.com/questions/7019283/automatically-type-cast-parameters-in-python
# by sequenceGeek (https://stackoverflow.com/users/525763/sequencegeek)
# (stackoverflow content is cc-wiki (aka cc-by-sa) licensed)
#
def _boolify(s):
    if s == 'True' or s == 'true':
        return True
    if s == 'False' or s == 'false':
        return False
    raise ValueError('Not Boolean Value!')


def _estimateType(var):
    '''guesses the str representation of the variables type'''
    var = str(var)  #important if the parameters aren't strings...
    for caster in (_boolify, int, float):
        try:
            return caster(var)
        except ValueError:
            pass
    return var


def _autocast(dFxn):
    def wrapped(*c, **d):
        cp = [_estimateType(x) for x in c]
        dp = dict((i, _estimateType(j)) for (i, j) in d.items())
        return dFxn(*cp, **dp)

    return wrapped

#
# End of stackoverflow content
#
