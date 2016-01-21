Brightway2 speedups
===================

A series of function written in `Cython <http://cython.org/>`__ that speed up critical functions to improve the overall performance of the `Brightway2 life cycle assessment framework <https://brightwaylca.org>`__.

In order to avoid having to have Cython as a dependency, this library includes both the ``pyx`` and Cython-generated ``c`` code, and is distributed as pre-compiled `wheels <https://pypi.python.org/pypi/wheel>`__, except on Linux where access to a ``C`` compiler is assumed.

Building ``C`` files
--------------------

cython -t bw2speedups/_consolidate.pyx bw2speedups/_indexer.pyx bw2speedups/_find_first.pyx

Building shared libraries
-------------------------

Although you can do this inplace, in my experience it is easier to just install the library in a temporary environment. You don't want to deal with ``.so`` files in the source repository.

Testing
-------

Install the library into a temporary environment, then manually run the separate test files, i.e. ``python bw2speedupds/test/test_consolidate.py``. This isn't the most elegant, but it will do for now.

Building wheels
---------------

pip install wheel
python setup.py bdist_wheel

Note that this has to be done separately for each OS and environment, i.e. Windows 32-bit and 64-bit versions of Python are separate wheels, even with the same version of Windows.
