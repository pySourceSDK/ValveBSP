from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from builtins import open
from builtins import range
from builtins import str
from future import standard_library
standard_library.install_aliases()

import collections
from shutil import copyfile  # NOQA: #402
from construct import *  # NOQA: #402
from valvebsp.constants import LUMP_GAME_LUMP  # NOQA: #402
import valvebsp.structs.bsp as BSP  # NOQA: #402

try:
    collectionsAbc = collections.abc
except AttributeError:
    collectionsAbc = collections


class Bsp(collectionsAbc.MutableMapping):
    """Contains all the data from a Bsp file"""

    def __init__(self, path=None, profile=None):
        """Creates an empty instance of Bsp.

        :param path: A path to an existing bsp file.
        :type path: str
        :param profile: A profile name corresponding to a specific game.
            :ref:`See profiles page for appropriate values<profiles>`
        :type profile: str, optional"""

        self.source_path = path
        self.profile = profile

        self.header = None
        self.lumps = {}

        # note: file might not be found,
        # profile might not exist
        if self.source_path:
            with open(path, 'rb') as f:
                header_struct = BSP.header(self.profile)
                self.header = header_struct.parse_stream(f)

    def save(self, destination=None):
        """Saves the current instance of the Bsp. Overwrites original bsp
        file if no destination is provided.

        Note that the bsp is lazy loaded. When overwritting, only loaded
        lumps will be written. When saving to a new destination,
        The original bsp will be copied and loaded lumps will be
        written on top.

        :param destination: A path (directory + filename) to determine
            where to save the bsp file.
        :type destination: str, optional
        """

        dest = destination or self.source_path
        try:
            d = open(dest, 'wb')
        except:
            raise FileNotFoundError

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
        kwargs['bspHeader'] = self.header
        return struct.parse_stream(f, **kwargs)

    def _parse_file(self, struct, **kwargs):
        kwargs['bspHeader'] = self.header
        return struct.parse_file(self.source_path, **kwargs)

    def _build_stream(self, struct, data, f, **kwargs):
        kwargs['bspHeader'] = self.header
        if not data:
            return
        return struct.build_stream(data, f, **kwargs)

    def _build_file(self, struct, data, **kwargs):
        if not struct:
            return
        kwargs['bspHeader'] = self.header
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
        """Provides data at the specified lump index. It is used for both
        bsp lumps (0, 1, 2, ...63) and game lumps ('prps', 'prpd', 'tlpd'...)

        :param index: The index of the lump.
        :type index: str, int
        """

        if index == '' or index == None:
            raise LumpUnsupportedError(index)

        if index not in range(0, 64) and \
           index not in ['prps', 'prpd', 'tlpd', 'hlpd']:
            raise LumpUnsupportedError(index)

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
