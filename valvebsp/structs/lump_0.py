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
from valvebsp.structs.common import *  # NOQA: #402


@lump_version(0)
def lump_0(header, profile=None):
    return GreedyString("ascii")
