import unittest
from sorts import *

class TestLab4(unittest.TestCase):

    def test_0(self):
        nums = [23, 10]
        comps = selection_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [10, 23])

    def test_1(self):
        val = [1,7,5,3,11]
        selection_sort(val)
        self.assertEqual(val, [1,3,5,7,11])

    def test_2(self):
        val = [1,7,5,3,11]
        insertion_sort(val)
        self.assertEqual(val, [1,3,5,7,11])

    def test_3(self):
        nums = [23, 10]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [10, 23])

    def test_empty(self):
        val1 = []
        self.assertEqual(insertion_sort(val1), 0)
        val2 = []
        self.assertEqual(selection_sort(val2), 0)
        self.assertEqual(val1, [])
        self.assertEqual(val2, [])

    def test_single(self):
        val1 = [1]
        val2 = [2]
        self.assertEqual(insertion_sort(val1), 0)
        self.assertEqual(selection_sort(val2), 0)
        self.assertEqual(val1, [1])
        self.assertEqual(val2, [2])

    def test_length(self):
        val1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 2, 15]
        val2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 2, 15]
        insertion_sort(val1)
        selection_sort(val2)
        self.assertEqual(val1, [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        self.assertEqual(val2, [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])


if __name__ == '__main__': 
    unittest.main()
