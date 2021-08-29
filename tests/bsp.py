import os
import sys
import unittest
import tempfile
import filecmp
from shutil import copyfile

from valvebsp.bsp import *
from valvebsp.constants import *


class ParseBspTestCase(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.bsp_file = os.path.join(self.test_dir, 'testmap.bsp')
        return

    def tearDown(self):
        return

    def test_struct_full_bsp(self):
        bsp = Bsp('tests/data/testmap.bsp', profile="TF2")

        for i in range(64):
            bsp[i]

        for gl in bsp[35].gamelump:
            bsp[gl.id]

        bsp.save(self.bsp_file)

        identical = filecmp.cmp('tests/data/testmap.bsp',
                                self.bsp_file,
                                shallow=False)

        self.assertTrue(identical)
    '''
    def test_struct_full_bsp_new(self):
        bsp = Bsp('tests/data/testmap.bsp', profile="TF2")

        for i in range(64):
            bsp[i]

        for gl in bsp[35].gamelump:
            bsp[gl.id]

        bsp.source_path = None
        bsp.save(self.bsp_file)

        identical = filecmp.cmp('tests/data/testmap.bsp',
                                self.bsp_file,
                                shallow=False)

        self.assertTrue(identical)
    '''

    def test_struct_partial_bsp_save_over(self):
        copyfile('tests/data/testmap.bsp', self.bsp_file)

        bsp = Bsp(self.bsp_file, profile="TF2")
        for i in [43, 6, 2]:
            bsp[i]
        bsp.save()

        identical = filecmp.cmp('tests/data/testmap.bsp',
                                self.bsp_file,
                                shallow=False)

        self.assertTrue(identical)

    def test_struct_partial_bsp_save_as(self):
        bsp = Bsp('tests/data/testmap.bsp', profile="TF2")
        for i in [43, 6, 2]:
            bsp[i]
        bsp.save(self.bsp_file)

        identical = filecmp.cmp('tests/data/testmap.bsp',
                                self.bsp_file,
                                shallow=False)

        self.assertTrue(identical)

    def test_struct_bsp_lost_impossible(self):
        bsp = Bsp('tests/data/testmap.bsp', profile="TF2")
        for i in range(64):
            bsp[i]
        for gl in bsp[35].gamelump:
            bsp[gl.id]
        bsp.source_path = None

        with self.assertRaises(Exception):
            bsp.save()

    def test_struct_bsp_overwrite_impossible(self):
        bsp = Bsp('tests/data/testmap.bsp', profile="TF2")
        for i in range(64):
            bsp[i]
        for gl in bsp[35].gamelump:
            bsp[gl.id]
        bsp.source_path = self.bsp_file

        with self.assertRaises(Exception):
            bsp.save()

    def test_struct_bsp_outofbound(self):
        bsp = Bsp('tests/data/testmap.bsp', profile="TF2")
        with self.assertRaises(LumpUnsupportedError):
            bsp[100]

        with self.assertRaises(LumpUnsupportedError):
            bsp[100] = ['pretending this is a lump']
