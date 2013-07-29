from setuptools.command import test

from .base import QipCommandBase


class test_unit (QipCommandBase):
    """Run unittests."""

    def __init__(self, distribution):
        self._test = test.test(distribution)
        QipCommandBase.__init__(self, distribution)

    def initialize_options(self):
        self._test.initialize_options()

    def finalize_options(self):
        self._test.finalize_options()

    def run(self):
        self._test.run()
