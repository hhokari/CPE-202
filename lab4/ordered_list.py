class Node:
    # Node for use with doubly-linked list
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

# A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of list)
class OrderedList:
    def __init__(self):
        # Creates a dummy node
        self.dummy = Node(None)
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy

    # Returns True is OrderedList is empty, False otherwise
    def is_empty(self):
        if self.dummy.prev == self.dummy:
            return True
        return False

    # Adds an item to OrderedList, in the proper location based on ordering of items
    # from lowest (at head of list) to highest (at tail of list)
    # If the item is already in the list, do not add it again
    def add(self, item):
        # creates a node with the item
        n = Node(item)
        current = self.dummy.next

        while current != self.dummy:
            # checks to see if the current item is less than the number to be added
            if current.item <= item:
                # if the item after the current item is the dummy node, add the item
                if current.next == self.dummy:
                    break
                # if the item after the current item is the dummy node, continue down the list
                elif current.next.item >= item:
                    break
            current = current.next
        # doesn't add the item if it's already in the list
        if current.item == item:
            pass
        # when adding an item, restructure the current links
        else:
            n.prev = current
            n.next = current.next
            current.next.prev = n
            current.next = n

    # Removes an item from OrderedList. If item is removed (was in the list) returns True
    # If item was not removed (was not in the list) returns False
    def remove(self, item):
        current = self.dummy.next
        while current != self.dummy:
            if current.item == item:
                current.next.prev = current.prev
                current.prev.next = current.next
                return True
            current = current.next
        return False

    # Returns index of an item in OrderedList (assuming head of list is index 0).
    def index(self, item):
        # Starts at index zero
        index = 0
        current = self.dummy.next
        # continues searching until end of the list is reached
        while current != self.dummy:
            # if the item is found, returns the index
            if current.item == item:
                return index
            index += 1
            current = current.next
        # If item is not in list, return None
        return None

    # Removes and returns item at index (assuming head of list is index 0).
    def pop(self, index):
        # If index is less than zero, raise IndexError
        if index < 0:
            raise IndexError
        # Starts at index zero
        current_index = 0
        current = self.dummy.next
        # Continues until the end of the list is reached, if the index is out of bounds, raises IndexError
        while current != self.dummy:
            # If the item is found, returns the item and reestablishes the links between the other Nodes
            if current_index == index:
                item = current.item
                current.next.prev = current.prev
                current.prev.next = current.next
                return item
            current_index += 1
            current = current.next
        raise IndexError

    # Searches OrderedList for item, returns True if item is in list, False otherwise"
    def search(self, item):
        return self.search_list(self.dummy.next, item)

    # a recursive method that steps through the list from head to tail
    def search_list(self, node, item):
        # returns False if the dummy node (end of list) is reached without finding the item
        if node == self.dummy:
            return False
        # returns True if the item is found
        if node.item == item:
            return True
        else:
            return self.search_list(node.next, item)

    # Returns a Python list representation of OrderedList, from head to tail
    def python_list(self):
        list = []
        # begins with the first item in the list
        current = self.dummy.next
        # continues to add items until the dummy node (end of list) is reached
        while current != self.dummy:
            list.append(current.item)
            current = current.next
        return list

    # Return a Python list representation of OrderedList, from tail to head, using recursion
    def python_list_reversed(self):
        rev_list = []
        return self.rev_list(self.dummy.prev, rev_list)

    # a recursive method that adds the last item of OrderedList to rev_list and then repeats
    def rev_list(self, node, rev_list):
        # returns the list if all the items in OrderedList have been added
        if node == self.dummy:
            return rev_list
        rev_list.append(node.item)
        return self.rev_list(node.prev, rev_list)

    # Returns number of items in the OrderedList
    def size(self):
        return self.find_size(self.dummy.next, 0)

    # a recursive method that goes through each item in the list and adds 1 to num_items
    # until the end is reached
    def find_size(self, node, num_items):
        # returns the number of items after reaching the end of the list
        if node == self.dummy:
            return num_items
        else:
            return self.find_size(node.next, num_items + 1)
