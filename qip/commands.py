import subprocess

from setuptools.command import test

from flake8.main import Flake8Command

from .cmdutils import QipCommandBase


def get_commands():
    return {
        'test': QipTestCommand,
        'test_unit': test.test,
        'test_flake8': Flake8Command,
        'test_doc': QipDocTestCommand,
        }


class QipTestCommand (QipCommandBase):
    """Run all Quality-Integrated-Packaging tests."""

    def run(self):
        print 'Hello!'
        import pprint ; raise NotImplementedError(pprint.pformat(vars(self.distribution)))


class QipDocTestCommand (QipCommandBase):
    """Run pyflakes."""

    def run(self):
        status = subprocess.call(['pyflakes', pkgname])
        if status != 0:
            raise SystemExit(status)



