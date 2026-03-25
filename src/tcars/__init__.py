__version__ = ""

from importlib.metadata import version, PackageNotFoundError
try:
    __version__ += version("tcars")
except PackageNotFoundError:
    # package is not installed
    pass

try:
    from tcars._ecrad_version import __ecrad_version__
    __version__ += f", ecrad-{__ecrad_version__}"
except:
    try:
        from ._ecrad_version import __ecrad_version__
        __version__ += f", ecrad-{__ecrad_version__}"
    except:
        pass
    pass

import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())
