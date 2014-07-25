import numpy as np
cimport numpy as np
cimport cython

DTYPE = np.uint32
ctypedef np.uint32_t DTYPE_t

@cython.boundscheck(False)
def indexer(np.ndarray[DTYPE_t, ndim=1] a, np.ndarray[DTYPE_t, ndim=1] b,
        mapping):
    cdef DTYPE_t MAX_INT_32 = 4294967295
    cdef int b_max = b.shape[0]
    for x in xrange(b_max):
        b[x] = mapping.get(a[x], MAX_INT_32)
    return True
