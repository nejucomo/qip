#! /usr/bin/env python

import os
from setuptools import setup, find_packages

cmdclass = {}
if not os.path.isfile('PKG-INFO'):
    # We are not in an sdist, so incorporate qip:
    import qip
    cmdclass.update(qip.get_commands())

# Else, we are in an unpacked sdist, so delegate to normal setuptools.


setup(name = 'qip',
      description = 'Quality Integrated Packaging - PEP440, pyflakes, style checking, unittest branch coverage, sdist installation testing.',
      url = 'https://github.com/nejucomo/qip',
      license = 'GPLv3',
      version = '0.1.dev0',
      author = 'Nathan Wilcox',
      author_email = 'nejucomo@gmail.com',
      packages = find_packages(),
      install_requires = ['flake8 >= 2.0', 'coverage >= 3.6'],
      test_suite = 'qip.tests',
      cmdclass = cmdclass,
      )
