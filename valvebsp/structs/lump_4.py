"""
Lump 4 - Visibility
===================

|lump_not_implemented|
"""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: #402
from valvebsp.structs.common import *  # NOQA: #402

'''
dvis_t = Struct(
    'numClusters' / Int32sl,
    'bitofs' / Int32sl[this.numclusters][2]
)
'''


@lump_raw
@lump_version(0)
def lump_4(header, profile=None):
    return
