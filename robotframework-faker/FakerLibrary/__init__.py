from importlib.metadata import version
from .keywords import FakerKeywords


__version__ = version("robotframework-faker")


class FakerLibrary(FakerKeywords):
    """

    """

    ROBOT_LIBRARY_SCOPE = "GLOBAL"
