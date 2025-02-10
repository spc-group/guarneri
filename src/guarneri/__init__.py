from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions

# TODO: fill this in with appropriate star imports:
__all__ = ["Instrument", "exceptions"]


from . import exceptions
from .instrument import Instrument
from .parsers import parse_config
