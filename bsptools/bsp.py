
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import range
from builtins import str
from builtins import open
from future import standard_library
standard_library.install_aliases()

from bsptools.bsp_struct import *  # NOQA: #402


LUMPS_UNSUPORTED = [4, 9, 10, 26, 27, 28, 29, 30, 31, 33, 34, 35,
                    36, 37, 38, 39, 40, 41, 46, 47, 48, 49, 61, 62, 63]
LUMPS_UNUSED = [22, 23, 24, 25, 32]


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
        if index not in range(64):
            raise IndexError("Lump ID out of range")
        if index in LUMPS_UNSUPORTED:
            raise IndexError("Lump ID not Supported")
        if index in LUMPS_UNUSED:
            raise IndexError("Lump ID is unused")
        if self.lumps[index]:
            return self.lumps[index]
        elif self.construct:
            self.lumps[index] = self.construct['lump_'+str(index)]()
            return self.lumps[index]

        else:
            return None
