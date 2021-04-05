"""
Lump 54 - Worldlights HDR
=========================

This lump contains an array of :any:`dworldlight_tV0` or :any:`dworldlight_tV1` (Version detection is automatic).
It is the HDR version of :ref:`lump 15<lump_15>`."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from valvebsp.structs.common import *  # NOQA #402
from valvebsp.structs.lump_15 import dworldlight_tV0, dworldlight_tV1  # NOQA #402


@lump_array
@lump_version([0, 1])
def lump_54(header, profile=None):
    if header.version == 0:
        return dworldlight_tV0
    elif header.version == 1:
        return dworldlight_tV1
