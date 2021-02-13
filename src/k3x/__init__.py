"""Package registration"""
from os import path

from .module1 import *

try:
    with open(path.join(path.dirname(__file__), "version.txt"), "r") as file:
        __version__ = file.readline().strip()
except:  # pylint: disable=bare-except
    __version__ = "0.0.dev0"

try:
    with open(path.join(path.dirname(__file__), "commit.txt"), "r") as file:
        __commit__ = file.readline().strip()
except:  # pylint: disable=bare-except
    __commit__ = "unknown"
