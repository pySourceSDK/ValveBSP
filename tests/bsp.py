import os
import sys
import unittest
import tempfile
import filecmp

from bsptools.bsp import *
from bsptools.bsp_struct import *  # NOQA: #402


class ParseBspTestCase(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.bsp_file = os.path.join(self.test_dir, 'testmap.bsp')
        return

    def tearDown(self):
        return

    def test_struct_bsp(self):
        bsp = Bsp('tests/data/testmap.bsp')

        for i in range(64):
            bsp[i]

        for gl in bsp.game_header.gamelump:
            bsp[gl.id]

        bsp.source_path = None
        bsp.save(self.bsp_file)

        identical = filecmp.cmp('tests/data/testmap.bsp',
                                self.bsp_file,
                                shallow=False)

        self.assertTrue(identical)
