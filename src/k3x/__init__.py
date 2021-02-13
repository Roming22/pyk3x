"""Package registration"""
from .module1 import *
from os import path

try:
    with open(path.join(path.dirname(__file__), "version.txt"), "r") as file:
        __version__ = file.readline().strip()
except:
    __version__ = "0.0.0-current_branch"