import os
import doctest

from .base import QipCommandBase


class test_doc (QipCommandBase):
    """Run doctests."""

    def run(self):
        for modpath in self._iter_module_paths():
            (modpart, _) = os.path.splitext(modpath)
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
