from .base import QipCommandBase


class QipTestCommand (QipCommandBase):
    """Run all Quality-Integrated-Packaging tests."""

    def run(self):
        for command in ['test_flake8', 'test_unit', 'test_doc']:
            self.distribution.run_command(command)
