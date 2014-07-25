import unittest
import numpy as np
from bw2speedups import indexer


class CIndicesFunctions(unittest.TestCase):
    def setUp(self):
        self.input_array = np.arange(5).astype(np.uint32)
        self.output_array = np.zeros((5,), dtype=np.uint32)
        self.mapping = dict([(x+1, x) for x in range(5)])
        self.reference = np.array((4294967295, 0, 1, 2, 3))

    def test_params_array(self):
        dtype = [('input', 'u4'), ('output', 'u4')]
        params = np.zeros((5,), dtype=dtype)
        for x in range(5):
            params['input'][x] = x
        indexer(params['input'], params['output'], self.mapping)
        self.assertTrue(np.allclose(self.reference, params['output']))

    def test_basic_lookup(self):
        indexer(self.input_array, self.output_array, self.mapping)
        self.assertTrue(np.allclose(self.reference, self.output_array))

    def test_dtype_remains_same(self):
        indexer(self.input_array, self.output_array, self.mapping)
        self.assertEqual(self.output_array.dtype, np.uint32)

    def test_id_remains_same(self):
        # Is there another way to check that no copying took place?
        input_id = id(self.output_array)
        indexer(self.input_array, self.output_array, self.mapping)
        self.assertEqual(id(self.output_array), input_id)


if __name__ == "__main__":
    unittest.main()
