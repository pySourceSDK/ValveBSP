"""
Header
======

The BSP file header is defined as a single :any:`dheader_t` (dheader_t variants are determined by :ref:`profile<profiles>`)
"""


from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function
from builtins import int
from future import standard_library
standard_library.install_aliases()


from construct import *	 # NOQA: #402
from valvebsp.constants import *  # NOQA: #402

lump_t_TF2 = Struct(
    'fileofs' / Int32sl,
    'filelen' / Int32sl,
    'version' / Int32sl,
    'uncompressedSize' / Int32sl
)

lump_t_L4D2 = Struct(
    'version' / Int32sl,
    'fileofs' / Int32sl,
    'filelen' / Int32sl,
    'fourCC' / Byte[4]
)

lump_t = Struct(
    'fileofs' / Int32sl,
    'filelen' / Int32sl,
    'version' / Int32sl,
    'fourCC' / Byte[4]
)

dheader_t_TITAN = Struct(
    'ident' / Const(b'VBSP'),
    'version' / Int32sl,
    'mapRevision' / Default(Int32sl, 0),
    'lump_count' / Const(127, Int32sl),
    'lump_t' / lump_t[this.lump_count],
)

dheader_t_TF2 = Struct(
    'ident' / Const(b'VBSP'),
    'version' / Int32sl,
    'lump_t' / lump_t_TF2[HEADER_LUMPS],
    'mapRevision' / Default(Int32sl, 0)
)

dheader_t_L4D2 = Struct(
    'ident' / Const(b'VBSP'),
    'version' / Int32sl,
    'lump_t' / lump_t_L4D2[HEADER_LUMPS],
    'mapRevision' / Default(Int32sl, 0)
)

dheader_t = Struct(
    'ident' / Const(b'VBSP'),
    'version' / Int32sl,
    'lump_t' / lump_t[HEADER_LUMPS],
    'mapRevision' / Default(Int32sl, 0)
)


def header(profile=None):
    if profile == TEAMFORTRESS2:
        return dheader_t_TF2
    elif profile in [LEFT4DEAD2, CONTAGION]:
        return dheader_t_L4D2
    elif profile == TITANFALL:
        return dheader_t_TITAN
    else:
        return dheader_t
