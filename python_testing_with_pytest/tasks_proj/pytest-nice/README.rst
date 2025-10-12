pytest-nice : A pytest plugin
=============================

Make pytest output a bit more friendly during failures.

Features
--------

- Includes the username of the person running tests in the pytest output.
- Adds a ``--nice`` option that:
  
  * Turns ``F`` into ``O`` (for *Opportunity*) in the short test summary.
  * With ``-v`` (verbose mode), changes ``FAILURE`` to 
    ``OPPORTUNITY for improvement``.

Installation
------------

Install via pip:

.. code-block:: bash

    pip install pytest-nice

Or install locally from source:

.. code-block:: bash

    pip install -e .

Usage
-----

Simply run:

.. code-block:: bash

    pytest --nice

Example output (short mode):

.. code-block:: text

    O..O

Example output (verbose mode):

.. code-block:: text

    OPPORTUNITY for improvement: test_example.py::test_something

Now every failure is just an *opportunity*! 😄
