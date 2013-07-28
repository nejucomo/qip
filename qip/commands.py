import subprocess

from setuptools.command import test

from .cmdbase import QipCommandBase
from .devdeps import Flake8Command


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
    """Run pyflakes."""

    def run(self):
        pkgname = 'FIXME'
        status = subprocess.call(['pyflakes', pkgname])
        if status != 0:
            raise SystemExit(status)
