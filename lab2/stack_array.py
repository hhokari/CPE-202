#
#Emily Gavrilenko
#015218875
#4/16/2019
#
#Lab 0
#Section 12
#This program creates a last-in first-out stack using an python list

class Stack:

    def __init__(self, capacity):
        #Creates and empty stack with a capacity
        self.capacity = capacity
        self.items = [None]*capacity
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
        # Returns True if the stack is full, and False otherwise

    def push(self, item):
        if self.num_items == self.capacity:
            raise IndexError
        # If stack is full when push is attempted, raises IndexError
        else:
            self.items[self.num_items] = item
            # adds the item to the top of the stack
            self.num_items += 1
            # increases stack size by one
        # If stack is not full, pushes item on stack.

    def pop(self):
        if self.num_items == 0:
            raise IndexError
        # If stack is empty when pop is attempted, raises IndexError
        else:
            value = self.items[self.num_items - 1]
            # stores the top item of the stack as value
            self.items[self.num_items - 1] = None
            # deletes the top item of the stack
            self.num_items -= 1
            # decreases the stack size by one
            return value
        # If stack is not empty, pops item from stack and returns item

    def peek(self):
        if self.num_items == 0:
            raise IndexError
        # If stack is empty, raises IndexError
        else:
            return self.items[self.num_items - 1]
        # If stack is not empty, returns the top item of the stack

    def size(self):
        return self.num_items

        # Returns the number of elements currently in the stack
