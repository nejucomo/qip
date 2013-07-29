import os
import doctest

from .base import QipCommandBase


class QipDocTestCommand (QipCommandBase):
    """Run doctests."""

    def run(self):
        for pkgname in sorted(self.distribution.packages):
            pkgpath = pkgname.replace('.', os.path.sep)
            for fname in sorted(os.listdir(pkgpath)):
                path = os.path.join(pkgpath, fname)
                (modpart, ext) = os.path.splitext(path)
                if ext == '.py':
                    modname = modpart.replace(os.path.sep, '.')
                    mod = self._import_leaf_mod(modname)
                    print '=== doctests for %r ===' % (modname,)
                    doctest.testmod(
                        mod,
                        name=modname,
                        report=True,
                        verbose=False)

    @staticmethod
    def _import_leaf_mod(modname):
        mod = __import__(modname)
        for modpart in modname.split('.')[1:]:
            mod = getattr(mod, modpart)
        return mod
