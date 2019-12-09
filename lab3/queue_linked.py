
class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class Queue:
    # Implements an link-based ,efficient first-in first-out Abstract Data Type
    def __init__(self, capacity):
        self.capacity = capacity
        self.num_items = 0
        self.first = None
        self.last = None

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
        # If the list is empty, makes item the first and last item of the list
        if self.num_items == 0:
            self.first = Node(item)
            self.last = self.first
            self.num_items += 1
        # If the list already has an item, adds the new item to the end of the list
        else:
            # If Queue is not full, enqueues (adds) item to Queue
            new_node = Node(item)
            # links the current last item to the newly passed item
            self.last.next = new_node
            # makes the newly passed item the last item
            self.last = new_node
            self.num_items += 1
        pass


    def dequeue(self):
        # If Queue is empty when dequeue is attempted, raises IndexError
        if self.num_items == 0:
            raise IndexError
        # If Queue is not empty, dequeues (removes) item from Queue and returns item.
        else:
            # Saves the first item as remove_item
            remove_item = self.first.data
            # links the current first item to the second item
            self.first = self.first.next
            self.num_items -= 1
            return remove_item


    def size(self):
        # Returns the number of elements currently in the Queue
        return self.num_items
