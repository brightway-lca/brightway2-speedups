#cython: language_level=3

import numpy as np
cimport numpy as np
cimport cython

DTYPE = np.uint8
ctypedef np.uint8_t DTYPE_t

try:
    _range = xrange
except NameError:
    _range = range


@cython.boundscheck(False)
def find_first(np.ndarray[DTYPE_t, ndim=1] a, b):
    """Replace each element of ``b`` with ``mapping.get(a, MAX_INT_32)``.

    Modifies numpy arrays in place.

    Much faster than plain python because of direct access without conversion to Numpy array."""
    cdef DTYPE_t value = b
    cdef int a_max = a.shape[0]
    for x in _range(a_max):
        if a[x] == value:
            return x
    return False
