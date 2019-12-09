import unittest
from queue_array import Queue
#from queue_linked import Queue

class TestLab1(unittest.TestCase):
    def test_queue(self):
        q = Queue(5)
        self.assertEqual(q.is_empty(), True)
        self.assertEqual(q.is_full(), False)
        q.enqueue('thing')
        self.assertEqual(q.dequeue(), 'thing')
        self.assertEqual(q.size(), 0)

    def test_queue1(self):
        q = Queue(3)
        with self.assertRaises(IndexError):  # uses context manager to check exception
            q.dequeue()
        q.enqueue('emily')
        q.enqueue('helene')
        self.assertEqual(q.size(), 2)
        q.dequeue()
        self.assertEqual(q.size(), 1)
        q.enqueue('serina')
        q.enqueue('dennis')
        self.assertEqual(q.is_empty(), False)
        self.assertEqual(q.is_full(), True)
        with self.assertRaises(IndexError):  # uses context manager to check exception
            q.enqueue('hello')
        self.assertEqual(q.dequeue(), 'helene')

    def test_queue2(self):
        q = Queue(3)
        q.enqueue('1')
        q.enqueue('2')
        q.enqueue('3')
        self.assertEqual(q.is_full(), True)
        q.dequeue()
        q.dequeue()
        q.enqueue('4')
        q.enqueue('5')
        self.assertEqual(q.dequeue(), '3')
        self.assertEqual(q.dequeue(), '4')

if __name__ == '__main__':
    unittest.main()

