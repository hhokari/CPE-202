#
#Emily Gavrilenko
#015218875
#5/22/2019
#
#Lab 7
#Section 12

class MaxHeap:

    def __init__(self, capacity=50):
        self.array = [None]*(capacity+1)
        self.capacity = capacity
        self.size = 0
        # Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created."""


    def enqueue(self, item):
        if self.size == self.capacity:
            return False
        index = self.size + 1
        self.array.insert(index, item)
        self.size += 1
        self.perc_up(index)
        return True
        # Inserts "item" into the heap, returns true if successful, false if there is no room in the heap"""


    def peek(self):
        if self.size == 0:
            return None
        return self.array[1]
        # Returns max without changing the heap, returns None if the heap is empty"""


    def dequeue(self):
        if self.size == 0:
            return None
        max = self.array[1]
        self.array[1] = self.array[self.size]
        self.perc_down(1)
        self.array.pop()
        self.size -= 1
        return max
        # Returns max and removes it from the heap and restores the heap property
        # Returns None if the heap is empty"""


    def contents(self):
        return self.array[1:]
        # Returns a list of contents of the heap in the order it is stored internal to the heap.
        # (This may be useful for in testing your implementation.)"""


    def build_heap(self, alist):
        if len(alist) > self.capacity:
            self.array = []*(self.capacity+1)
            self.capacity = len(alist)
        index = len(alist)//2
        self.array = [None] + alist
        self.size = len(alist)
        while index > 0:
            self.perc_down(index)
            index -= 1
        return self.array[1:]
        # Builds a heap from the items in alist and builds a heap using the bottom up method.
        # If the capacity of the current heap is less than the number of
        # items in alist, the capacity of the heap will be increased"""


    def is_empty(self):
        if self.size is 0:
            return True
        return False
        # Returns True if the heap is empty, false otherwise"""


    def is_full(self):
        if self.size == self.capacity:
            return True
        return False
        # Returns True if the heap is full, false otherwise"""

        
    def get_capacity(self):
        return self.capacity
        # This is the maximum number of a entries the heap can hold
        # 1 less than the number of entries that the array allocated to hold the heap can hold"""
    
    
    def get_size(self):
        return self.size
        # Returns the actual number of elements in the heap, not the capacity"""

    def find_max_child(self, index):
        if index*2 == self.size:
            return index*2
        right_child = self.array[index*2+1]
        left_child = self.array[index*2]
        if right_child > left_child:
            return index*2+1
        else:
            return index*2
        # Returns the index of the maximum value between the left and right child

    def perc_down(self, i):
        if i*2 <= self.size:
            max_child = self.find_max_child(i)
            if self.array[i] < self.array[max_child]:
                parent = self.array[i]
                child = self.array[max_child]
                self.array[max_child] = parent
                self.array[i] = child
                self.perc_down(max_child)
        # Where the parameter i is an index in the heap and perc_down moves the element stored
        # at that location to its proper place in the heap rearranging elements as it goes."""


    def perc_up(self, i):
        if self.array[i//2]is not None:
            if self.array[i] > self.array[i//2]:
                parent = self.array[i//2]
                child = self.array[i]
                self.array[i] = parent
                self.array[i//2] = child
                self.perc_up(i//2)
        # Where the parameter i is an index in the heap and perc_up moves the element stored
        # at that location to its proper place in the heap rearranging elements as it goes."""


    def heap_sort_ascending(self, alist):
        self.build_heap(alist)
        index = len(alist)-1
        while self.size > 0:
            alist[index] = self.dequeue()
            index -= 1
        return alist
        # Perform heap sort on input alist in ascending order
        # This method will discard the current contents of the heap, build a new heap using
        # the items in alist, then mutate alist to put the items in ascending order"""


