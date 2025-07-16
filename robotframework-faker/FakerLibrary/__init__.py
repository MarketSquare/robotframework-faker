from importlib.metadata import version
from .keywords import FakerKeywords


__version__ = version("robotframework-faker")


class FakerLibrary(FakerKeywords):
    """

    """

    ROBOT_LIBRARY_SCOPE = "GLOBAL"
    __doc__ = f"""
    Robot Framework keyword library wrapper for Faker.

    This set of keywords was generated using Faker version {version("Faker")}.
    """

