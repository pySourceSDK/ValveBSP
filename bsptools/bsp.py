
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import str
from builtins import open
from future import standard_library
standard_library.install_aliases()

from bsptools.bsp_struct import *  # NOQA: #402


class Bsp(object):
    """Contains all the data from a Bsp file"""

    def __init__(self, path=None):
        """Creates an empty instance of Bsp."""

        self.ident = None
        self.version = None
        self.offsets = None
        self.mapRevision = None
        self.lumps = [None] * 64
        self.construct = None

        if path:
            self.f = open(path, "rb")
            self.construct = bsp_t.parse_stream(self.f)

            self.ident = self.construct['ident']
            self.version = self.construct['version']
            self.lump_t = self.construct['lump_t']
            self.mapRevision = self.construct['mapRevision']

    def __getitem__(self, index):
        if self.lumps[index]:
            return self.lumps[index]
        elif self.construct:
            self.lumps[index] = self.construct['lump_'+str(index)]()
            return self.lumps[index]

        else:
            return None
