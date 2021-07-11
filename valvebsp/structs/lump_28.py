"""
Lump 28 - Phys Disp
===================

|lump_not_implemented|
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: #402
from valvebsp.structs.common import *  # NOQA #402

physdisp = Struct(
    'registry' / PrefixedArray(Int16ul,
                               Struct('count' / Byte, 'unused' / Byte)),
    'bytestreams' / Array(lambda ctx: len(ctx.registry),
                          Bytes(lambda ctx: ctx.registry[ctx._index].count))
)


@lump_version(0)
def lump_28(header, profile=None):
    return physdisp
