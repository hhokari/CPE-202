import unittest

# Use the imports below to test either your array-based stack
# or your link-based version
from stack_array import Stack
# from stack_linked import Stack

class TestLab2(unittest.TestCase):
    def test_simple(self):
        stack = Stack(5)
        stack.push(0)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(), 1)
    def test2(self):
        stack = Stack(4)
        self.assertTrue(stack.is_empty())
        stack.push(None)
        stack.push(4)
        stack.push(1)
        stack.push(7)
        self.assertTrue(stack.is_full())
        self.assertEqual(stack.pop(), 7)
        self.assertEqual(stack.size(), 3)
    def test3(self):
        stack = Stack(2)
        with self.assertRaises(IndexError):  # uses context manager to check exception
            stack.pop()
        with self.assertRaises(IndexError):  # uses context manager to check exception
            stack.peek()
        stack.push(3)
        self.assertNotEqual(stack.peek(), 2)
        stack.push(2)
        self.assertEqual(stack.peek(), 2)
        with self.assertRaises(IndexError):  # uses context manager to check exception
            stack.push(7)
    def test4(self):
        stack = Stack(3)
        stack.push(None)
        self.assertEqual(stack.peek(), None)
        stack.push(3)
        stack.push(-2)
        stack.pop()
        stack.pop()
        stack.pop()
        self.assertEqual(stack.size(), 0)


if __name__ == '__main__': 
    unittest.main()
