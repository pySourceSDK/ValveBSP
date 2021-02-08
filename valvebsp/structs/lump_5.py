"""
Lump 5 - Nodes
==============
"""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: #402
from valvebsp.constants import *  # NOQA: #402
from valvebsp.exceptions import *  # NOQA: #402
from valvebsp.structs.common import *  # NOQA #402

dnode_t = Aligned(4, Struct(
    'planeNum' / Int32sl,
    'children' / Int32sl[2],
    'mins' / Int16sl[3],
    'maxs' / Int16sl[3],
    'firstFace' / Int16ul,
    'numFaces' / Int16ul,
    'area' / Int16sl,
))


def lump_5(header, profile=None):
    if header.version != 0:
        raise LumpVersionUnsupportedError(header.version)
    return lump_array(LUMP_NODES, dnode_t, header)
