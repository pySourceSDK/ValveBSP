"""
Lump 59 - Map Flags
===================

This lump contains a single :any:`flags_t`.
"""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: #402
from valvebsp.structs.common import *  # NOQA #402
from valvebsp.structs.flags import levelflags_flags32  # NOQA: #402

flags_t = Struct('levelFlags' / levelflags_flags32)


@lump_struct
@lump_version(0)
def lump_59(header, profile=None):
    return flags_t
