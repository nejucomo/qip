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
      description = 'Quality Integrated Packaging - PEP440, pyflakes, style checking, unittesting, sdist install testing.',
      url = 'https://github.org/nejucomo/qip',
      license = 'GPLv3',
      version = '0.1.dev0',
      author = 'Nathan Wilcox',
      author_email = 'nejucomo@gmail.com',
      packages = find_packages(),
      install_requires = [],
      cmdclass = cmdclass,
      )
