import unittest
from lab1 import *

class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        tlist = [10, 9, 8, 4, 9]
        self.assertEqual(max_list_iter(tlist), 10) #searches for max number in front
        tlist = [9, 8, 10, 4, 9]
        self.assertEqual(max_list_iter(tlist), 10) #searches for max number in middle
        tlist = [5, 9, 8, 4, 10]
        self.assertEqual(max_list_iter(tlist), 10) #searches for max number in the end
        tlist = [-10, -9, -1, -4, -9]
        self.assertEqual(max_list_iter(tlist), -1) #searches for negative max number
        tlist = []
        self.assertEqual(max_list_iter(tlist), None) #searches None list that raises ValueError
        tlist = None
        with self.assertRaises(ValueError):
            max_list_iter(tlist)

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1]) #reverses list with odd number of entries
        self.assertEqual(reverse_rec([3,2,1]),[1,2,3]) #reverses list with even number of entries
        self.assertEqual(reverse_rec([-3,2,-1,5]),[5,-1,2,-3])
        #reverses list with negative and positive entries
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(tlist)
        #reverses None list and raises Error
        tlist = []
        self.assertEqual(reverse_rec(tlist), None)
        #reverses empty list and returns None


    def test_bin_search_middle_of_list(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, low, high, list_val), 4 )
        #Searches for target in the middle of the list

    def test_bin_search_not_in_list(self):
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(6, low, high, list_val), None)
        # Searches for target not in the list

    def test_bin_search_in_end_list(self):
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(7, low, high, list_val), 5)
        # Searches for target in the end portion of the list

    def test_bin_search_in_beginning_list(self):
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(1, low, high, list_val), 1)
        # Searches for target in the beginning portion of the list

    def test_bin_search_empty_list(self):
        list_val = []
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(4, low, high, list_val), None)
        # Searches for target in an empty list, returns None

    def test_bin_search_None_list(self):
        list_val = None
        low = 0
        high = 2
        with self.assertRaises(ValueError):
            bin_search(4, low, high, list_val)
        # Searches for target in None list, raises Error message

    def test_bin_search_before_list(self):
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(-10, low, high, list_val), None)
        # Searches for target less than low

    def test_bin_search_after_list(self):
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(20, low, high, list_val), None)
        # Searches for target greater than high

    def test_bin_search_negative_list(self):
        list_val = [-10,-7,-4,-3,-2,0]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(-7, low, high, list_val), 1)
        # Searches for negative target



if __name__ == "__main__":
        unittest.main()