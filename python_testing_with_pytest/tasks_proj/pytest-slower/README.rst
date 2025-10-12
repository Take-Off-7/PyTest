pytest-duration-check : A pytest plugin
=======================================

Detect slow-running tests by comparing their execution time across runs.

Features
--------

- Records how long each test takes to execute.
- On the next run, if a test takes **more than 2× longer than before**, it **fails automatically**.
- Helps catch performance regressions early.

Installation
------------

Install locally in editable mode::

    pip install -e .

Usage
-----

Simply run pytest as usual — no extra flags needed::

    pytest

If a test suddenly becomes slower than before, you'll see a failure like::

    AssertionError: test duration over 2x last duration

Now every slowdown becomes a warning sign — before it becomes a problem! 🚀
