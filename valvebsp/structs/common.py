"""
Common Structures
=================

These are reoccuring data structures that you'll see reused throughout Bsp.
"""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: E402
from valvebsp.constants import *  # NOQA: E402
from valvebsp.exceptions import *  # NOQA: #402

import collections
try:
    Iterable = collections.abc.Iterable
except AttributeError:
    Iterable = collections.Iterable


Vector = Struct('x' / Float32l, 'y' / Float32l, 'z' / Float32l)


Vector2D = Struct('x' / Float32l, 'y' / Float32l)
Vector4D = Struct('x' / Float32l, 'y' / Float32l,
                  'z' / Float32l, 'w' / Float32l)
RadianEuler = Struct('x' / Float32l, 'y' / Float32l, 'z' / Float32l)
QAngle = Struct('x' / Float32l, 'y' / Float32l, 'z' / Float32l)
Quaternion = Struct('x' / Float32l, 'y' / Float32l,
                    'z' / Float32l, 'w' / Float32l)
color32 = Struct('r' / Int8ul, 'g' / Int8ul, 'b' / Int8ul, 'a' / Int8ul)
ColorRGBExp32 = Struct('r' / Byte, 'g' / Byte, 'b' /
                       Byte, 'exponent' / Int8sl)
CompressedLightCube = Array(6, ColorRGBExp32)


def lump_version(versions):
    # helper for lump version validation
    def decorator(func):
        def wrapper(*args, **kwargs):
            requested_version = args[0].version
            supported_versions = versions
            if not isinstance(versions, Iterable):
                supported_versions = [versions]
            if requested_version not in supported_versions:
                raise LumpVersionUnsupportedError(requested_version)
            return func(*args, **kwargs)
        return wrapper
    return decorator


def lump_raw(func):
    # helper for raw or unsupported lumps
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return GreedyBytes
    return wrapper


def lump_struct(func):
    # helper for struct based lumps
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).compile()
    return wrapper


def lump_array(func):
    # helper for array based lumps
    def wrapper(*args, **kwargs):
        return GreedyRange(func(*args, **kwargs).compile())
    return wrapper


def lump_prefixed_array(prefix):
    # helper for prefixed array based lumps
    def decorator(func):
        def wrapper(*args, **kwargs):
            return PrefixedArray(prefix, func(*args, **kwargs))
        return wrapper
    return decorator
