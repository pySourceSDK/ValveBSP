"""
Lump 28 - Phys Disp
===================

This lump contains a single :any:`physdisps`. 'registry' and 'bytestreams' are of equal length. the length of each bytestream is determined by the corresponding length stated in the registry. The format of the bytestream is not currently known/implemented and will return raw bytes.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: #402
from valvebsp.structs.common import *  # NOQA #402

streamLength = Struct('length' / Byte, 'unused' / Byte)

physdisps = Struct(
    'registry' / PrefixedArray(Int16ul, streamLength),
    'bytestreams' / Array(lambda ctx: len(ctx.registry),
                          Bytes(lambda ctx: ctx.registry[ctx._index].length))
)


@lump_version(0)
def lump_28(header, profile=None):
    return physdisps
