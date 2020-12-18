# stdlib
import sys


__version__ = "0.3"

try:
    from .base import BaseAnonymizer, lazy_attribute  # noqa: F401
    from .utils import *  # noqa: F401,F403

except ImportError:
    # During setup.py not all dependencies may be installed, which may cause some
    # imports to fail. We still need to be able to import __init__ to check __version__,
    # as this is considered a good practice (having __version__ inside __init__)
    #
    # That's the cost of having shorthands like:
    #
    # >>> import anon
    # >>> anon.BaseAnonymizer
    #
    # versus having to import from base:
    #
    # >>> from anon.base import BaseAnonymizer
    # >>> BaseAnonymizer
    #
    if not sys.argv[0].endswith("setup.py"):
        raise
