"""
Lump 0 - Entities
=================

This lump is simply one long string containing all entities in a format similar to vmf.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: #402
from valvebsp.constants import *  # NOQA: #402
from valvebsp.exceptions import *  # NOQA: #402
from valvebsp.structs.common import *  # NOQA: #402

entities = Struct(
    'content' / Aligned(4, CString("ascii"))
)


def lump_0(header, profile=None):
    if header.version != 0:
        raise LumpVersionUnsupportedError(header.version)
    return Pointer(header.fileofs, entities)
