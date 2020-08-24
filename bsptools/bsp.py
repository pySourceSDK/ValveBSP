
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from builtins import dict
from builtins import object
from builtins import range
from builtins import str
from builtins import open
from future import standard_library
standard_library.install_aliases()

from shutil import copyfile  # NOQA: #402
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
                self.header = BSP.header.parse_stream(f)
                self.game_header = BSP.lump_35.parse_stream(
                    f, lump_header=self.header.lump_t[35])

    def save(self, dest=None):

        dest = dest or self.source_path
        if not dest:
            raise FileNotFoundError

        d = open(dest, 'wb')

        if not self.source_path:
            self._build_stream(BSP.header, self.header, d)

        elif dest != self.source_path:
            s = open(self.source_path, 'rb')
            d.write(s.read())
            s.close()

        for index, val in enumerate(self.lumps):
            lump_struct = getattr(BSP, 'lump_' + str(index))
            lump_header = self._get_lump_header(index)
            self._build_stream(lump_struct, val, d, lump_header=lump_header)

        for key in self.game_lumps.keys():
            val = self.game_lumps[key]
            lump_struct = getattr(BSP, 'lump_' + str(key))
            lump_header = self._get_lump_header(key)
            self._build_stream(lump_struct, val, d, lump_header=lump_header)

        d.close()

    def _parse_stream(self, struct, f, **kwargs):
        kwargs['header'] = self.header
        return struct.parse_stream(f, **kwargs)

    def _parse_file(self, struct, **kwargs):
        kwargs['header'] = self.header
        return struct.parse_file(self.source_path, **kwargs)

    def _build_stream(self, struct, data, f, **kwargs):
        kwargs['header'] = self.header
        if not data:
            return
        return struct.build_stream(data, f, **kwargs)

    def _build_file(self, struct, data, **kwargs):
        if not struct:
            return
        kwargs['header'] = self.header
        return struct.build_file(data, self.source_path, **kwargs)

    def _get_lump_header(self, index):
        if isinstance(index, str):  # It's a gamelump id
            for h in self.game_header.gamelump:
                if h.id == index:
                    return h

        elif isinstance(index, int):  # It's a lump number
            if index in range(64) and self.header:
                return self.header.lump_t[index]

        raise IndexError('Invalid Lump ID')

    def __setitem__(self, key, value):
        return

    def __getitem__(self, index):

        lump_header = self._get_lump_header(index)
        struct = getattr(BSP, 'lump_' + str(index))

        data = self._parse_file(struct, lump_header=lump_header)

        if isinstance(index, str):
            self.game_lumps[index] = data
            return self.game_lumps[index]
        elif isinstance(index, int):
            self.lumps[index] = data
            return self.lumps[index]
        else:
            return None

    def __delitem__(self, key):
        del self.store[self.__keytransform__(key)]

    def __iter__(self):
        return self.item(self.lumps)

    def __len__(self, index):
        return 64

    def __keytransform__(self, key):
        return key
