
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
from bsptools.constants import LUMP_GAME_LUMP  # NOQA: #402
import bsptools.bsp_struct as BSP  # NOQA: #402

GAMELUMP_SUPPORTED = {
    'prps': dict([(10, BSP.StaticPropLump_t)]),
    'prpd': dict([(4, BSP.DetailPropLump_t)]),
    'tlpd': dict([(0, BSP.DetailPropLightStylesLump_t)]),
    'hlpd': dict([(0, BSP.DetailPropLightStylesLump_t)])
}


class Bsp(MutableMapping):
    """Contains all the data from a Bsp file"""

    def __init__(self, path=None):
        """Creates an empty instance of Bsp."""

        self.source_path = None
        self.header = None
        self.game_header = None

        self.lumps = [None] * 64
        self.game_lumps = {}

        if path:
            self.source_path = path
            with open(path, 'rb') as f:
                self.header = self._parse_stream(f, BSP.header)
                self.game_header = self._parse_stream(f, BSP.lump_35)

    def _parse_stream(self, f, struct):
        return struct.parse_stream(f, header=self.header)

    def _parse_file(self, struct):
        return struct.parse_file(self.source_path, header=self.header)

    def __setitem__(self, key, value):
        return

    def __getitem__(self, index):

        if isinstance(index, str):  # It's a gamelump id

            if index not in self.game_lumps:
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

                self.game_lumps[index] = self._parse_file(gamelump)
            return self.game_lumps[index]

        elif isinstance(index, int):  # It's a lump id

            if index not in range(64):
                raise IndexError("Lump ID out of range")
            if not self.lumps[index]:
                if self.header:
                    lump_n = getattr(BSP, 'lump_' + str(index))
                    self.lumps[index] = self._parse_file(lump_n)
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
