Contributing
============

Few things to know before diving in the code.

Project Guidelines
------------------

Be pythonic, document and test your code. That's all.


Dev Environment
---------------

To tinker with the code, it's recommended that you install the library from the cloned folder with:

.. code-block:: bash

   pip install --editable .


This will allow you to install |proj_name| from the folder. This way, you can modify |proj_name| as you develop your own project around it.

Documenting
-----------
The documentation is done with `Sphinx <http://www.sphinx-doc.org/en/master/>`_.
To build the Sphinx documentation, you need:

.. code-block:: bash

   pip install -r docs/requirements.txt # one-time setup

   sphinx-autobuild docs/source docs/build

The documentation pages will be served on http://127.0.0.1:8000 by default.


Testing
-------
Tests can be ran from the root folder using:

.. code-block:: bash

   pip install -r requirements.txt # one-time setup

   pytest
