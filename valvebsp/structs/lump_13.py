"""
Lump 13 - Surfedges
===================

This lump contains an array of :any:`Int<int>`. The absolute value references the edge array (:ref:`lump_12<lump_12>`). Positive values indicate the edge is defined from the first to second vertex. Negative values indicate the edge is defined from second to first vertex.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: #402
from valvebsp.structs.common import *  # NOQA: #402


@lump_array
@lump_version(0)
def lump_13(header, profile=None):
    return Int32sl
