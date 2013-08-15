import os
import errno

from coverage import coverage
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
        try:
            os.mkdir('dist')
        except os.error, e:
            if e.errno != errno.EEXIST:
                raise
            # Else: It already exists, no problem.
        else:
            print "Created 'dist' directory."

        covdata = os.path.join('dist', 'coverage.data')
        covreport = os.path.join('dist', 'coverage_html')

        print 'Recording test coverage in %r' % (covdata,)
        cov = coverage(
            data_file=covdata,
            data_suffix=False,
            cover_pylib=False,
            auto_data=False,
            timid=False,
            branch=True,
            config_file=False,
            source=self.distribution.packages,
            omit=None,
            include=None,
            )

        cov.start()
        try:
            try:
                self._test.run()
            finally:
                cov.stop()

                print 'Reporting test coverage in %r' % (covreport,)
                cov.html_report(directory=covreport)
        except SystemExit, se:
            if se.args != (0,):
                raise
            # Else, continue running other commands.
