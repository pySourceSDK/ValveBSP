Profiles
========

.. _profiles:

Profiles exist for games featuring alternative implementations of "mainline" bsp lump versions. if you can't find the game you're working for in this list, either the game is fully in line with the "mainline" source branch or it's not currently supported.

.. automodule:: valvebsp.profiles
   :members:



Usage
-----
You are not required to use the profile constants, they exist mostly for reference.

These are Equivalent:

.. code-block:: bash

   from valvebsp.profiles import PROFILES
   bsp = Bsp('map.bsp', profiles['TEAMFORTRESS2'])

.. code-block:: bash

   from valvebsp.profiles import TEAMFORTRESS2
   bsp = Bsp('map.bsp', TEAMFORTRESS2)

.. code-block:: bash

   bsp = Bsp('map.bsp', 'TF2')
