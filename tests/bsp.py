import os
import unittest

from bsptools import *
from bsptools.parser import *


class ParseBspTestCase(unittest.TestCase):
    def setUp(self):
        return

    def tearDown(self):
        return

    def test_struct_bsp(self):
        with open('/mnt/archive/releases/cp_vanguard_a2.bsp', "rb") as f:
            results = bsp_t.parse_stream(f)
            print(results.lump_1)
        self.assertTrue(True)
