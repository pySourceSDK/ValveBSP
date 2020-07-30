from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import dict
from builtins import object
from builtins import range
from builtins import str
from builtins import open
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: #402
from collections.abc import MutableMapping  # NOQA: #402
from bsptools.bsp_struct import *  # NOQA: #402

GAMELUMP_SUPPORTED = {
    'prps': dict([(10, StaticPropLump_t)]),
    'prpd': dict([(4, DetailPropLump_t)]),
    'tlpd': dict([(0, DetailPropLightStylesLump_t)]),
    'hlpd': dict([(0, DetailPropLightStylesLump_t)])
}


class Bsp(MutableMapping):
    """Contains all the data from a Bsp file"""

    def __init__(self, path=None):
        """Creates an empty instance of Bsp."""

        self.ident = None
        self.version = None
        self.offsets = None
        self.mapRevision = None
        self.lumps = [None] * 64
        self.gamelumps = {}
        self.source_path = None
        self.construct = None

        if path:
            self.f = open(path, "rb")
            self.source_path = path
            self.construct = bsp_t.parse_stream(self.f)

            self.ident = self.construct['ident']
            self.version = self.construct['version']
            self.lump_t = self.construct['lump_t']
            self.mapRevision = self.construct['mapRevision']

    def __setitem__(self, key, value):
        return

    def __getitem__(self, index):

        if isinstance(index, str):  # It's a gamelump id

            if index not in self.gamelumps:
                gamelump = False
                for lump in self[LUMP_GAME_LUMP].gamelump:
                    if lump.id == index and \
                       index in GAMELUMP_SUPPORTED:
                        if lump.version not in GAMELUMP_SUPPORTED[index]:
                            raise IndexError('Lump version not supported')

                        gamelump = Pointer(
                            lump.fileofs, GAMELUMP_SUPPORTED[index][lump.version])
                        continue
                if not gamelump:
                    raise IndexError('Lump ID not Found')

                self.gamelumps[index] = gamelump.parse_stream(self.f)

            return self.gamelumps[index]

        elif isinstance(index, int):  # It's a lump id

            if index not in range(64):
                raise IndexError("Lump ID out of range")
            if not self.lumps[index]:
                if self.construct:
                    self.lumps[index] = self.construct['lump_'+str(index)]()
                else:
                    return None

            if index == 40:
                return bytearray(self.lumps[index])

            return self.lumps[index]

    def __delitem__(self, key):
        del self.store[self.__keytransform__(key)]

    def __iter__(self):
        return self.item(self.lumps)

    def __len__(self, index):
        return 64

    def __keytransform__(self, key):
        return key
