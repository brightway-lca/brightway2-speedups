import unittest
import numpy as np
from bw2speedups import consolidate


class ConsolidateTestCase(unittest.TestCase):
    # def setUp(self):
    #     self.input_array = np.arange(5).astype(np.uint32)
    #     self.output_array = np.zeros((5,), dtype=np.uint32)
    #     self.mapping = dict([(x+1, x) for x in range(5)])
    #     self.reference = np.array((4294967295, 0, 1, 2, 3))

    def test_main(self):
        # a = np.array((-1, 0, 1)).astype(float)
        # b = np.array((-0.5, 0.5))
        a = np.array((-2, 0, 2)).astype('timedelta64[s]')
        b = np.array((-1, 1)).astype('timedelta64[s]')        
        c = (a.reshape((-1, 1)) + b.reshape((1, -1))).ravel()
        d = np.arange(6).astype(float)
        # e, f = consolidate(c, d)
        # self.assertTrue(np.allclose(e, np.array((-1.5, -.5, .5, 1.5))))
        e, f = consolidate(c.view('int64'), d)
        # self.assertTrue(np.allclose(e.astype('timedelta64[s]'), np.array((-3, -1, 1, 3), dtype='timedelta64[s]')))
        self.assertTrue(np.array_equal(e.astype('timedelta64[s]'), np.array((-3, -1, 1, 3), dtype='timedelta64[s]')))
        self.assertTrue(np.allclose(f, np.array((0, 3, 7, 5))))

    def test_shapes(self):
        #a = np.array((0.5, 1.5, 2.5))
        #b = np.array((-0.5, 0.5))
        a = np.array((0.5, 1.5, 2.5)).astype('timedelta64[s]') 
        b = np.array((-0.5, 0.5))
        with self.assertRaises(AssertionError):
            consolidate(a.view('int64'), b)
            #consolidate(a, b)

if __name__ == "__main__":
    unittest.main()
