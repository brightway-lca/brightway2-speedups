Brightway2 speedups
===================

A series of function written in `Cython <http://cython.org/>`__ that speed up critical functions to improve the overall performance of the `Brightway2 life cycle assessment framework <http://brightway2.readthedocs.org/en/latest/>`__.

In order to avoid having to have Cython as a dependency, this library includes both the ``pyx`` and Cython-generated ``c`` code, and is distributed as pre-compiled `wheels <https://pypi.python.org/pypi/wheel>`__, except on Linux where access to a ``C`` compiler is assumed.

Building ``C`` files
--------------------

cython -t bw2speedups/_consolidate.pyx bw2speedups/_indexer.pyx bw2speedups/_find_first.pyx

Building shared libraries
-------------------------

Although you can do this inplace, in my experience it is easier to just install the library in a temporary environment. You don't want to deal with ``.so`` files in the source repository.

Testing
-------

Install the library into a temporary environment, then manually run the separate test files, i.e. ``python bw2speedupds/test/test_consolidate.py``. This isn't the most elegant, but

Building wheels
---------------

