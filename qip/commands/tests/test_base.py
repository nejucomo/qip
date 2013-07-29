import unittest

from qip.commands import base


class DescriptionFromDocPropertyTests (unittest.TestCase):
    def setUp(self):

        class C (object):
            """some doc"""

            desc = base.DescriptionFromDocProperty()

        self.cls = C
        self.obj = C()

    def test_get_from_class(self):
        self.assertEqual(self.cls.__doc__, self.cls.desc)

    def test_get_from_instance(self):
        self.assertEqual(self.cls.__doc__, self.obj.desc)


class QipCommandBaseTests (unittest.TestCase):
    pass
