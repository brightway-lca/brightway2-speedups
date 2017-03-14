import numpy as np
cimport numpy as np
cimport cython

TTYPE= np.int64
VTYPE = np.float64

ctypedef np.int64_t TTYPE_t
ctypedef np.float64_t VTYPE_t 

try:
    _range = xrange
except NameError:
    _range = range

@cython.boundscheck(False)
def consolidate(np.ndarray[TTYPE_t, ndim=1] a,
                np.ndarray[VTYPE_t, ndim=1] b):
    """Consolidate an index array and values array, summing elements in the values array for each unique element of the index array.

    For example:

    .. code-block:: python

        import numpy as np
        a = np.array((0.5, 1, 2, 2, -1, -1)).astype('timedelta64[s]')
        b = np.arange(6).astype(float)

    Would return:

    .. code-block:: python

        np.array([-1, 0.5, 1, 2], dtype='timedelta64[s]'),
        np.array((9, 0, 1, 5))

    ``a``, the index array, must by one-dimensional NumPy arrays with dtype ``timedelta64[s]`` and ``b``, the value array, must by one-dimensional NumPy arrays with dtype ``float64``.

    Returns:
        Consolidated sorted index array and consolidated values array.

    """
    #integration of timedelta based on http://stackoverflow.com/questions/33522626/using-datetime-and-bool-in-cython
    #it works with view so `times.view('int64')` has to be passed to consolidate instead of `times`
    assert a.shape[0] == b.shape[0]
    index_values = np.unique(a)
    index_values.sort()
    cdef int new_shape = index_values.shape[0]
    cdef np.ndarray[TTYPE_t, ndim=1] c = \
            np.zeros(new_shape, dtype=TTYPE)
    cdef np.ndarray[VTYPE_t, ndim=1] d = \
            np.zeros(new_shape, dtype=VTYPE)

    for index in _range(new_shape):
        c[index] = index_values[index]
        d[index] = b.take(np.where(a == index_values[index])).sum()
    #c.view need to be reconverted to 'timedelta64[s]' in __mul__ and __add__
    return c.view('timedelta64[s]'), d  
