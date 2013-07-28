"""Import all development dependencies in one place to handle import errors consistently."""

__all__ = ['Flake8Command']

_RequirementsMessage = """Missing qip dependencies.

This package relies on qip - Quality Integrated Packaging.

If you wish to install this package as a user, please install from PyPI
with pip >= 1.4, or from an official sdist tarball.

If you wish to develop this package or create releases, please install
these dependencies:

  pip install 'flake8 >= 2.0'
"""


try:
    from flake8.main import Flake8Command
except ImportError:
    raise SystemExit(_RequirementsMessage)

