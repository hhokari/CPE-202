class TreeNode:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

class BinarySearchTree:

    def __init__(self):
        # Returns empty BST
        self.root = None

    def is_empty(self):
        # returns True if tree is empty, else False
        if self.root is None:
            return True
        return False

    def search(self, key):
        # returns True if key is in a node of the tree, else False
        return self.search_help(key, self.root)

    def search_help(self, key, tree_root):
        if self.root is None:
            return False
        if tree_root.key == key:
            return True
        left = tree_root.left
        right = tree_root.right
        if left is not None:
            if self.search_help(key, left) == True:
                return True
        if right is not None:
            if self.search_help(key, right) == True:
                return True
        return False

    def insert(self, key, data=None):
        # inserts new node with key and data
        node = TreeNode(key, data)
        if self.root is None:
            self.root = node
        else:
            current = self.root
            self.insert_help(current, node)

    def insert_help(self, current, new_node):
        # If an item with the given key is already in the BST,
        # the data in the tree will be replaced with the new data
        if new_node.key == current.key:
            current.data = new_node.data
        # If an item's key is greater than the current item, goes right
        if new_node.key > current.key:
            # Adds the new_node to the right of the current node if it's empty
            if current.right is None:
                current.right = new_node
            else:
                self.insert_help(current.right, new_node)
        # If an item's key is greater than the current item, goes right
        if new_node.key < current.key:
            # Adds the new_node to the left of the current node if it's empty
            if current.left is None:
                current.left = new_node
            self.insert_help(current.left, new_node)

    def find_min(self):
        # returns a tuple with min key and data in the BST
        # returns None if the tree is empty
        if self.root is None:
            return None
        else:
            current = self.root
            return self.min(current)

    def min(self, node):
        # Helping method for finding the min recursively
        if node.left is None:
            return (node.key, node.data)
        return self.min(node.left)

    def find_max(self):
        # returns a tuple with max key and data in the BST
        # returns None if the tree is empty
        if self.root is None:
            return None
        else:
            current = self.root
            return self.max(current)

    def max(self, node):
        # Helping method for finding the max recursively
        if node.right is None:
            return (node.key, node.data)
        return self.max(node.right)

    def tree_height(self):
        # return the height of the tree
        # returns None if tree is empty
        if self.root is None:
            return None
        else:
            node = self.root
            index = 0
            return self.height(node, index)

    def height(self, node, index):
        # returns height when at the bottom node
        if node.left is None and node.right is None:
            return index
        # finds the biggest height by traveling through all the possible
        # left and right branches are returning the greatest index
        if self.height_left(node, index) >= self.height_right(node, index):
            return self.height_left(node, index)
        else:
            return self.height_right(node, index)

    def height_left(self, node, index):
        # determines if there is another height layer on the left
        if node.left is None:
            return index
        else:
            index += 1
            return self.height(node.left, index)

    def height_right(self, node, index):
        # determines if there is another height layer on the right
        if node.right is None:
            return index
        else:
            index += 1
            return self.height(node.right, index)

    def inorder_list(self):
        in_order = []
        if self.root is None:
            return in_order
        # return Python list of BST keys representing in-order traversal of BST
        return self.in_order(self.root, in_order)

    # returns a list in order by viewing nodes in order of left, root, right
    def in_order(self, node, list):
        if node.left is None:
            list.append(node.key)
        elif node.left is not None:
            self.in_order(node.left, list)
            list.append(node.key)
        if node.right is not None:
            self.in_order(node.right, list)
        return list

    def preorder_list(self):
        # return Python list of BST keys representing pre-order traversal of BST
        pre_order = []
        if self.root is None:
            return pre_order
        # return Python list of BST keys representing in-order traversal of BST
        return self.pre_order(self.root, pre_order)

    def pre_order(self, node, list):
        list.append(node.key)
        if node.left is not None:
            self.pre_order(node.left, list)
        if node.right is not None:
            self.pre_order(node.right, list)
        return list
        
    def delete(self, key):
        # deletes node containing key
        # Returns True if the item was deleted, False otherwise
        if self.search_help(key, self.root) is False:
            return False
        current = self.root
        return self.delete_help(key, current)

    # Recursive function that helps delete the node with the given key
    def delete_help(self, key, parent):
        # Sets the node equal to None if it doesn't have any children
        if key == self.root.key and self.root.left is None and self.root.right is None:
            self.root = None
            return True
        # searches the left branch for the key to be deleted
        if parent.left is not None:
            if parent.key == key:
                if self.check_no_grandchildren(parent.left) is True:
                    parent.key = parent.left.key
                    parent.left = None
                    return True
                self.delete_child(parent)
                return True
            elif parent.left.key == key:
                child = parent.left
                self.add_parent(child, parent)
                # If the the node to be deleted has no children,
                # delete the parent's reference to the child
                if child.left is None and child.right is None:
                    self.parent(child).left = None
                    return True
                # If the node to be deleted has children,
                # replace it with another number from the binary tree
                else:
                    self.delete_child(child)
                    return True
        # searches the right branch for the key to be deleted
        if parent.right is not None:
            if parent.key == key:
                if self.check_no_grandchildren(parent.right) is True:
                    parent.key = parent.right.key
                    parent.right = None
                    return True
                self.delete_child(parent)
                return True
            elif parent.right.key == key:
                child = parent.right
                self.add_parent(child, parent)
                # If the the node to be deleted has no children,
                # delete the parent's reference to the child
                if child.left is None and child.right is None:
                    self.parent(child).right = None
                    return True
                # If the node to be deleted has children,
                # replace it with another number from the binary tree
                else:
                    self.delete_child(child)
                    return True

        # Assigns the parent node as the left or right child
        if parent.left is not None:
            if self.search_help(key, parent.left) is True:
                return self.delete_help(key, parent.left)
        if parent.right is not None:
            if self.search_help(key, parent.right) is True:
                return self.delete_help(key, parent.right)
        # return True

    def check_no_grandchildren(self, node):
        if node.left is None and node.right is None:
            return True
        return False

    def add_parent(self, node, parent):
        node.parent = parent

    def parent(self, node):
        return node.parent


    def delete_child(self, current):
        # replaces the node to be deleted with the maximum number on the left
        # and deletes the replaced value
        if current.left is not None:
            maximum = current.left
            self.add_parent(maximum, current)
            if self.check_no_grandchildren(maximum) is True:
                current.key = maximum.key
                current.data = maximum.data
                self.parent(maximum).left = None
                return True
            while maximum.right is not None:
                self.add_parent(maximum.right, maximum)
                maximum = maximum.right
            current.key = maximum.key
            current.data = maximum.data
            if self.check_no_grandchildren(maximum) is True:
                self.parent(maximum).right = None
                return True
            self.delete_help(maximum.key, current.left)
        # replaces the node to be deleted with the minimum number on the right
        # and deletes the replaced value
        else:
            minimum = current.right
            self.add_parent(minimum, current)
            if self.check_no_grandchildren(minimum)is True:
                current.key = minimum.key
                current.data = minimum.data
                self.parent(minimum).right = None
                return True
            while minimum.left is not None:
                self.add_parent(minimum.left, minimum)
                minimum = minimum.left
            current.key = minimum.key
            current.data = minimum.data
            if self.check_no_grandchildren(minimum) is True:
                self.parent(minimum).left = None
                return True
            self.delete_help(minimum.key, current.right)