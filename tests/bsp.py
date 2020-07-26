import os
import unittest

from bsptools.bsp import *


class ParseBspTestCase(unittest.TestCase):
    def setUp(self):
        return

    def tearDown(self):
        return

    def test_struct_bsp(self):
        with open('/mnt/archive/releases/cp_vanguard_a2.bsp', "rb") as f:
            results = bsp_t.parse_stream(f)
            print(results.lump_1)
        print(bsp[58])
        self.assertTrue(True)
