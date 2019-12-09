#
#Emily Gavrilenko
#015218875
#4/16/2019
#
#Lab 0
#Section 12
#This program creates a last-in first-out stack using a linked list

class Node:
    # creates a Node where data can be stored and referenced
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self, capacity):
        #Creates and empty stack with a capacity
        self.capacity = capacity
        self.head = None
        self.num_items = 0

    def is_empty(self):
        if self.num_items == 0:
            return True
        return False
    #Returns True if the stack is empty, and False otherwise

    def is_full(self):
        if self.num_items == self.capacity:
            return True
        return False
    #Returns True if the stack is full, and False otherwise

    def push(self, item):
        if self.num_items == self.capacity:
            raise IndexError
        #If stack is full when push is attempted, raises IndexError
        else:
            if self.head is None:
                self.head = Node(item)
                self.num_items += 1
            # creates a Node with the input item and calls it the head if the head was previously None
            else:
                new_node = Node(item)
                new_node.next = self.head
                self.head = new_node
                self.num_items += 1
        #If stack is not full, pushes item on stack.

    def pop(self):
        if self.num_items == 0:
            raise IndexError
        # If stack is empty when pop is attempted, raises IndexError
        else:
            value = self.head.data
            # stores item to be removed as value
            self.head = self.head.next
            # changes the head to the previous item on the stack
            self.num_items -= 1
            return value
    # If stack is not empty, pops item from stack and returns item.

    def peek(self):
        if self.num_items == 0:
            raise IndexError
        # If stack is empty, raises IndexError
        else:
            return self.head.data
    # If stack is not empty, returns head item

    def size(self):
        return self.num_items
    # Returns the number of elements currently in the stack

 