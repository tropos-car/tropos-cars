__version__ = ""

from importlib.metadata import version, PackageNotFoundError
try:
    __version__ += version("tcars")
except PackageNotFoundError:
    # package is not installed
    pass

try:
    import _ecrad_version
    __version__ += f", ecrad-{_ecrad_version.__version__}"
except PackageNotFoundError:
    # package is not installed
    pass

import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())
