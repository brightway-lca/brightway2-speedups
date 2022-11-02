#cython: language_level=3

import numpy as np
cimport numpy as np
cimport cython

DTYPE = np.uint32
ctypedef np.uint32_t DTYPE_t

try:
    _range = xrange
except NameError:
    _range = range


@cython.boundscheck(False)
def indexer(np.ndarray[DTYPE_t, ndim=1] a, np.ndarray[DTYPE_t, ndim=1] b,
            mapping):
    """Replace each element of ``b`` with ``mapping.get(a, MAX_INT_32)``.

    Modifies numpy arrays in place.

    Much faster than plain python because of direct access without conversion to Numpy array."""
    cdef DTYPE_t MAX_INT_32 = 4294967295
    cdef int b_max = b.shape[0]
    for x in _range(b_max):
        b[x] = mapping.get(a[x], MAX_INT_32)
    return True
