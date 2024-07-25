Quickstart
==========

Get yourself up and running quickly.

Installation
------------

PyPI
~~~~
|proj_name| is available on the Python Package Index. This makes installing it with pip as easy as:

.. code-block:: bash

   pip3 install valvebsp

Git
~~~

If you want the latest code or even feel like contributing, the code is available on GitHub.

You can easily clone the code with git:

.. code-block:: bash

   git clone git://github.com/pySourceSDK/ValveBSP.git

and install it from the repo directory with:

.. code-block:: bash

   python3 setup.py install

Usage
-----

Here's a few example usage of |proj_name|

Parsing
~~~~~~~

Parsing can be done by creating an instance of Bsp with a path.

.. code-block:: python

   > from valvebsp import Bsp

   > bsp = Bsp('C:/Program Files (x86)/Steam/steamapps/common/Team Fortress 2/tf/maps/ctf_2fort.bsp')
