from .commands.test import test
from .commands.test_unit import test_unit
from .commands.test_flake8 import test_flake8
from .commands.test_doc import test_doc


QipCommands = [test, test_unit, test_flake8, test_doc]


def get_commands():
    return dict((cls.__name__, cls) for cls in QipCommands)
