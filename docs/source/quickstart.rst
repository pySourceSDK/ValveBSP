Quickstart
==========

Get yourself up and running quickly.

Installation
------------

PyPI
~~~~
Bsp-tools is available on the Python Package Index. This makes installing it with pip as easy as:

.. code-block:: bash

   pip3 install bsptools

Git
~~~

If you want the latest code or even feel like contributing, the code is available on GitHub.

You can easily clone the code with git:

.. code-block:: bash

   git clone git://github.com/maxdup/bsp-tools.git

and install it with:

.. code-block:: bash

   python3 setup.py install

Usage
-----

Here's a few example usage of bsp-tools

Parsing
~~~~~~~

Parsing can be done by creating an instance of Bsp with a path.

.. code-block:: python

   > from bsptools import BspParse

   > bsp = Bsp('C:/Program Files (x86)/Steam/steamapps/common/Team Fortress 2/tf/maps/ctf_2fort.bsp')
