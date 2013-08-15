import os

from setuptools import Command


class DescriptionFromDocProperty (property):
    def __get__(self, _, cls):
        return cls.__doc__


class QipCommandBase (Command):
    """no options and delegate description to the subclass __doc__."""

    description = DescriptionFromDocProperty()

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    # Utilities for subclasses:
    def _iter_package_dirs(self):
        for pkgname in sorted(self.distribution.packages):
            yield pkgname.replace('.', os.path.sep)

    def _iter_module_paths(self):
        for pkgdir in self._iter_package_dirs():
            for fname in sorted(os.listdir(pkgdir)):
                path = os.path.join(pkgdir, fname)
                if path.endswith('.py'):
                    yield path
