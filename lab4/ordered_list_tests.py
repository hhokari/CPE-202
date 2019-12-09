import unittest
from ordered_list import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        t_list = OrderedList()
        self.assertEqual(t_list.python_list_reversed(), [])
        self.assertTrue(t_list.is_empty())
        t_list.add(10)
        self.assertEqual(t_list.index(10), 0)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.python_list_reversed(), [10])
        self.assertEqual(t_list.size(), 1)
        t_list.add(5)
        t_list.add(7)
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list(), [5, 7, 10])
        t_list.add(100)
        self.assertEqual(t_list.python_list(), [5, 7, 10, 100])
        t_list.add(5)
        self.assertEqual(t_list.python_list(), [5, 7, 10, 100])
        self.assertEqual(t_list.size(), 4)
        self.assertEqual(t_list.index(10), 2)
        self.assertEqual(t_list.index(-7), None)
        self.assertEqual(t_list.index(700), None)
        self.assertEqual(t_list.index(4), None)
        self.assertEqual(t_list.python_list_reversed(), [100, 10, 7, 5])
        self.assertEqual(t_list.search(5), True)
        self.assertEqual(t_list.search(1), False)
        self.assertTrue(t_list.remove(10))
        self.assertFalse(t_list.remove(2))
        self.assertEqual(t_list.size(), 3)
        self.assertEqual(t_list.pop(2), 100)
        self.assertEqual(t_list.size(), 2)
        with self.assertRaises(IndexError):  # uses context manager to check exception
            t_list.pop(-2)
        with self.assertRaises(IndexError):  # uses context manager to check exception
            t_list.pop(9)
        self.assertEqual(t_list.pop(0), 5)

    def test_1(self):
        t_list = OrderedList()
        self.assertTrue(t_list.is_empty())
        t_list.add(10)
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.index(10), 0)
        self.assertTrue(t_list.search(10))
        self.assertEqual(t_list.python_list_reversed(), [10])
        self.assertTrue(t_list.remove(10))
        self.assertFalse(t_list.remove(2))
        t_list.add(10)
        self.assertEqual(t_list.pop(0), 10)


if __name__ == '__main__': 
    unittest.main()
