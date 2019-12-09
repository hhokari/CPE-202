#
#Emily Gavrilenko
#015218875
#6/10/2019
#
#Project 5
#Section 12

import unittest
from graph import *

class TestList(unittest.TestCase):
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

    def test_01(self):
        g = Graph('test1.txt')
        self.assertEqual(g.get_vertex(10), None)
        self.assertEqual(g.get_vertex("v1"), g.vertices["v1"])
        self.assertEqual(g.get_vertices(), ['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9'])
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']])
        self.assertTrue(g.is_bipartite())
        
    def test_02(self):
        g = Graph('test2.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3'], ['v4', 'v6', 'v7', 'v8']])
        self.assertFalse(g.is_bipartite())

    def test_03(self):
        g = Graph('test1.txt')
        g.add_vertex("v10")
        g.add_edge("v9", "v10")
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5'], ['v10', 'v6', 'v7', 'v8', 'v9']])
        self.assertTrue(g.is_bipartite())

    def test_04(self):
        # create_new_text("text3.txt")
        g = Graph('text3.txt')
        self.assertEqual([['v1', 'v2','v3'], ['v4', 'v5', 'v6']], g.conn_components())
        self.assertFalse(g.is_bipartite())

if __name__ == '__main__':
   unittest.main()
