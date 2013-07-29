import os
import doctest

from setuptools.command import test
from flake8.main import Flake8Command

from .cmdbase import QipCommandBase


def get_commands():
    return {
        'test': QipTestCommand,
        'test_unit': test.test,
        'test_flake8': QipFlake8Command,
        'test_doc': QipDocTestCommand,
        }


class QipTestCommand (QipCommandBase):
    """Run all Quality-Integrated-Packaging tests."""

    def run(self):
        for command in ['test_flake8', 'test_unit', 'test_doc']:
            self.distribution.run_command(command)


class QipFlake8Command (Flake8Command):
    def run(self):
        try:
            Flake8Command.run(self)
        except SystemExit, e:
            if e.args != (0,):
                raise
            # Otherwise continue with other setup.py commands.


class QipDocTestCommand (QipCommandBase):
    """Run doctests."""

    def run(self):
        for pkgname in sorted(self.distribution.packages):
            pkgpath = pkgname.replace('.', os.path.sep)
            for fname in sorted(os.listdir(pkgpath)):
                path = os.path.join(pkgpath, fname)
                (modpart, ext) = os.path.splitext(path)
                if ext == '.py':
                    modname = modpart.replace(os.path.sep, '.')
                    mod = self._import_leaf_mod(modname)
                    print '=== doctests for %r ===' % (modname,)
                    doctest.testmod(
                        mod,
                        name=modname,
                        report=True,
                        verbose=False)

    @staticmethod
    def _import_leaf_mod(modname):
        mod = __import__(modname)
        for modpart in modname.split('.')[1:]:
            mod = getattr(mod, modpart)
        return mod
