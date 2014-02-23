
from distutils.core import setup

setup(
    name='robotframework-faker',
    packages=['robotframework-faker'],  # this must be the same as the name above
    version='0.1',
    description='Robot Framework wrapper for faker, a fake test data generator',
    author='Guy Kisel',
    author_email='guy.kisel@gmail.com',
    url='https://github.com/guykisel/robotframework-faker',
    keywords='robotframework testing test automation faker',  # arbitrary keywords
    classifiers=[],
    install_requires=['fake-factory', 'robotframework'],
    long_description=open('README.md').read(),
    license=open('LICENSE').read(),
)
