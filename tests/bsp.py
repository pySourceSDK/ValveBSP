import os
import unittest

from bsptools.bsp import *


class ParseBspTestCase(unittest.TestCase):
    def setUp(self):
        return

    def tearDown(self):
        return

    def test_struct_bsp(self):
        bsp = Bsp('/mnt/archive/releases/cp_vanguard_b7.bsp')
        print(bsp[58])
        self.assertTrue(True)
