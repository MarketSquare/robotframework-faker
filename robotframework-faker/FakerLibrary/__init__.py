import pkg_resources
from keywords import FakerKeywords
__author__ = 'gkisel'


__version__ = pkg_resources.get_distribution("robotframework-faker").version


class FakerLibrary(FakerKeywords):
    """

    """
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
