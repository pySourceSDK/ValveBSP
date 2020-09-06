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
import bsptools.structs.bsp_struct as BSP  # NOQA: #402


class Bsp(MutableMapping):
    """Contains all the data from a Bsp file"""

    def __init__(self, path=None, profile=None):
        """Creates an empty instance of Bsp."""

        self.source_path = path
        self.profile = profile
        self.header = None
        self.lumps = {}

        if self.source_path:
            with open(path, 'rb') as f:
                header_struct = BSP.header(self.profile)
                self.header = header_struct.parse_stream(f)

    def save(self, dest=None):

        dest = dest or self.source_path
        if not dest:
            raise FileNotFoundError

        d = open(dest, 'wb')

        if not self.source_path:
            header_struct = BSP.header(self.profile)
            self._build_stream(header_struct, self.header, d)

        elif dest != self.source_path:
            s = open(self.source_path, 'rb')
            d.write(s.read())
            s.close()

        for key in self.lumps.keys():
            val = self.lumps[key]
            lump_header = self._get_lump_header(key)
            lump_fn = getattr(BSP, 'lump_' + str(key))
            lump_struct = lump_fn(lump_header, self.profile)
            self._build_stream(lump_struct, val, d)

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
            for h in self[35].gamelump:
                if h.id == index:
                    return h
        elif isinstance(index, int):  # It's a lump number
            if index in range(64) and self.header:
                return self.header.lump_t[index]

        raise IndexError('Invalid Lump ID (' + str(index) + ')')

    def __getitem__(self, index):

        if index == '' or index == None:
            return None

        if index in self.lumps and self.lumps[index]:
            return self.lumps[index]

        lump_header = self._get_lump_header(index)
        lump_fn = getattr(BSP, 'lump_' + str(index))
        lump_struct = lump_fn(lump_header, self.profile)
        data = self._parse_file(lump_struct)
        self.lumps[index] = data

        return self.lumps[index]

    def __setitem__(self, key, value):
        return

    def __delitem__(self, key):
        del self.store[self.__keytransform__(key)]

    def __iter__(self):
        return self.item(self.lumps)

    def __len__(self, index):
        return 64

    def __keytransform__(self, key):
        return key
