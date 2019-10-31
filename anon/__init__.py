# noqa: F401
import sys

__version__ = "0.1"

try:
    from .base import BaseAnonymizer, lazy_attribute
    from .utils import *
except ImportError:
    if not sys.argv[0].endswith('setup.py'):
        raise
