from .commands.test import QipTestCommand
from .commands.test_unit import QipUnitTestCommand
from .commands.test_flake8 import QipFlake8Command
from .commands.test_doc import QipDocTestCommand


def get_commands():
    return {
        'test': QipTestCommand,
        'test_unit': QipUnitTestCommand,
        'test_flake8': QipFlake8Command,
        'test_doc': QipDocTestCommand,
        }
