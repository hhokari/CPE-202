class Queue:
    # Implements an array-based, first-in first-out Abstract Data Type using a python array

    def __init__(self, capacity):
        # creates an empty queue with a capacity
        self.items = [None]*capacity
        self.capacity = capacity
        self.last = 0
        self.first = 0
        self.num_items = 0

    def is_empty(self):
        # Returns True if the Queue is empty, and False otherwise
        if self.num_items == 0:
            return True
        return False

    def is_full(self):
        # Returns True if the Queue is full, and False otherwise
        if self.num_items == self.capacity:
            return True
        return False

    def enqueue(self, item):
        # If Queue is full when enqueue is attempted, raises IndexError
        if self.num_items == self.capacity:
            raise IndexError
        else:
            # If Queue is not full, adds item to the end of the Queue
            self.items[self.last] = item
            # Changes the end of the queue to the next spot in the list
            # If the list capacity is reached, the end of the list circles back to index 0
            self.last = (self.last+1) % self.capacity
            self.num_items += 1


    def dequeue(self):
        # If Queue is empty when dequeue is attempted, raises IndexError
        if self.num_items == 0:
            raise IndexError
        else:
            # If Queue is not empty, dequeues (removes) item from Queue and returns item.
            item = self.items[self.first]
            # stores the first item in the value as item
            self.items[self.first] = None
            # deletes the first item from the Queue
            self.first = (self.first + 1) % self.capacity
            self.num_items -= 1
            return item
            # returns the first item

    def size(self):
        # Returns the number of elements currently in the Queue, not the capacity
        return self.num_items
        pass
