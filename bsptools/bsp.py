from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()


class Bsp(object):
    """Contains all the data from a Bsp file"""

    def __init__(self):
        """Creates an empty instance of Bsp."""

        self.id = None
        self.version = None
