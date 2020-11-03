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

   pip3 install --editable .


This will allow you to import the bsptools in other projects normally while being able to mess with the code directly from the git folder. This way, you can make sure bsptools will work as intended in the context of your project.


Documenting
-----------
The documentation is done with `Sphinx <http://www.sphinx-doc.org/en/master/>`_.
To build the Sphinx documentation, you need:

.. code-block:: bash

   pip install -U sphinx
   pip install sphinx-autobuild

Then you can run sphinx-autobuild.sh in the docs/ directory. The documentation pages will be served on http://127.0.0.1:8000 by default.


Testing
-------
Tests can be ran from the root folder using:

.. code-block:: bash

   python3 tests/tests.py
