from setuptools.command import test

from .commands import QipTestCommand, QipFlake8Command, QipDocTestCommand


def get_commands():
    return {
        'test': QipTestCommand,
        'test_unit': test.test,
        'test_flake8': QipFlake8Command,
        'test_doc': QipDocTestCommand,
        }
