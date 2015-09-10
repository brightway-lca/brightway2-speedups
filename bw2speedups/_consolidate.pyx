import numpy as np
cimport numpy as np
cimport cython

DTYPE = np.float64
ctypedef np.float64_t DTYPE_t

try:
    _range = xrange
except NameError:
    _range = range


@cython.boundscheck(False)
def consolidate(np.ndarray[DTYPE_t, ndim=1] a,
                np.ndarray[DTYPE_t, ndim=1] b):
    """Consolidate an index array and values array, summing elements in the values array for each unique element of the index array.

    For example:

    .. code-block:: python

        import numpy as np
        a = np.array((0.5, 1, 1.5, 1.5, -1, -1))
        b = np.arange(6).astype(float)

    Would return:

    .. code-block:: python

        np.array((-1, 0.5, 1, 1.5)),
        np.array((9, 0, 1, 5))

    Both ``a``, the index array, and ``b``, the value array, must by one-dimensional NumPy arrays with dtype ``float64``.

    Returns:
        Consolidated sorted index array and consolidated values array.

    """
    assert a.shape[0] == b.shape[0]
    index_values = np.unique(a)
    index_values.sort()
    cdef int new_shape = index_values.shape[0]
    cdef np.ndarray[np.float64_t, ndim=1] c = \
            np.zeros(new_shape, dtype=np.float64)
    cdef np.ndarray[np.float64_t, ndim=1] d = \
            np.zeros(new_shape, dtype=np.float64)

    for index in _range(new_shape):
        c[index] = index_values[index]
        d[index] = b.take(np.where(a == index_values[index])).sum()

    return c, d
