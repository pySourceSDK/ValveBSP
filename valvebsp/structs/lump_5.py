"""
Lump 5 - Nodes
==============

This lump contains an array of :any:`dnode_t`.
"""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: #402
from valvebsp.structs.common import *  # NOQA #402

dnode_t = Aligned(4, Struct(
    'planeNum' / Int32sl,
    'children' / Int32sl[2],
    'mins' / Int16sl[3],
    'maxs' / Int16sl[3],
    'firstFace' / Int16ul * 'index into :ref:`lump 7<lump_7>`',
    'numFaces' / Int16ul,
    'area' / Int16sl,
))


@lump_array
@lump_version(0)
def lump_5(header, profile=None):
    return dnode_t
