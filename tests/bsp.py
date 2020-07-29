import os
import sys
import unittest

from bsptools.bsp import *


class ParseBspTestCase(unittest.TestCase):
    def setUp(self):
        return

    def tearDown(self):
        return

    def test_struct_bsp(self):
        bsp = Bsp('tests/data/testmap.bsp')
        print(bsp[35])
        print(bsp['prps'])

        self.assertTrue(True)
