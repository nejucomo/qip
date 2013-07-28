__all__ = ['setup', 'find_packages']


# Direct forwards from setuptools:
# The design goal is packages can do search/replace from "setuptools"
# to "qip" in their setup.py to integrate qip.

from setuptools import find_packages


from .setupfunc import setup
