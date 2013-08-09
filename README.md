============================
Quality Integrated Packaging
============================

The Goal
========

By adding a minimal fragment to your python project's
[setuptools](https://pypi.python.org/pypi/setuptools/0.9.8)-based
`setup.py`, you get a bunch of quality assurance features:

./setup.py test
---------------

 * PEP440 checking of the version.
 * PEP8 style checking.
 * pyflakes checking.
 * unit tests with html coverage report.

./setup.py sdist
----------------

 * Verify all of the above test targets in a clean virtualenv install
   from an sdist.
 * No dependency on `qip` for `sdist` or other distribution formats.
 * Ensure your package is signed with the proper `GPG`
   key. [1](#footnote-1) [2](#footnote-2)
 * Further quality checks on `sdist` not caught by the standard
   `setuptools`, such as:
   + Fail on `MANIFEST.in` patterns which match no existing files.

<a id="footnote-1" href="#footnote-1">1.</a> There is no good signature
verification scheme for python packaging at the moment.

<a id="footnote-2" href="#footnote-2">2.</a> Be the first on your block
to sign all of your packages!
