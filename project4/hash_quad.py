#
#Emily Gavrilenko
#015218875
#6/4/2019
#
#Project4
#Section 12

class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:

    def __init__(self, table_size):          # can add additional attributes
        self.table_size = table_size         # initial table size
        self.hash_table = [None]*table_size  # hash table
        self.num_items = 0                   # empty hash table

    def insert(self, key, value=0):
        value = value
        val = self.horner_hash(key)
        index = int(self.quad_prob(val, key))
        if self.hash_table[index] is None:
            try:
                val = int(value)
                item = Item(key, [val])
            except TypeError:
                item = Item(key, value)
            except ValueError:
                item = Item(key, [value])
            self.hash_table[index] = item
            self.num_items += 1
        elif self.hash_table[index].key == key:
            value_list = self.hash_table[index].value
            if value_list[-1] != value:
                thing = self.hash_table[index]
                array = thing.value
                array.append(value)
                new_item = Item(key, array)
                self.hash_table[index] = new_item
        if self.get_load_factor() > 0.5:
            list = self.hash_table
            self.table_size = self.table_size * 2 + 1
            self.num_items = 0
            self.hash_table = [None] * self.table_size
            for i in list:
                if i is not None:
                    self.insert(i.key, i.value)
        """ Inserts an entry into the hash table (using Horner hash function to determine index, 
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value is the line number that the word appears on. 
        If the key is not already in the table, then the key is inserted, and the value is used as the first 
        line number in the list of line numbers. If the key is in the table, then the value is appended to that 
        key’s list of line numbers. If value is not used for a particular hash table (e.g. the stop words hash table),
        can use the default of 0 for value and just call the insert function with the key.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased (doubled + 1)."""

    def quad_prob(self, index, key):
        val = 0
        while self.hash_table[(index + val*val) % self.table_size] is not None:
            if self.hash_table[(index + val*val) % self.table_size].key == key:
                return (index + val*val) % self.table_size
            val += 1
        return (index + val*val) % self.table_size

    def find_min(self, key):
        if len(key) < 8:
            return len(key)
        return 8
        # Returns the minimum between len(key) and 8

    def horner_hash(self, key):
        min = self.find_min(key)
        index = 0
        output = 0
        while index < min:
            output += ord(key[index])*pow(31, min-1-index)
            index += 1
        return output%self.table_size
        # Compute and return an integer from 0 to the (size of the hash table) - 1
        # Compute the hash value by using Horner’s rule, as described in project specification.

    def in_table(self, key):
        index = self.horner_hash(key)
        if self.hash_table[index] is not None:
            if self.hash_table[index].key == key:
                return True
            val = 1
            while self.hash_table[(index + val * val) % self.table_size] is not None:
                if self.hash_table[(index + val * val) % self.table_size].key == key:
                    return True
                val += 1
        return False
        # Returns True if key is in an entry of the hash table, False otherwise."""

    def get_index(self, key):
        index = self.horner_hash(key)
        if self.hash_table[index] is not None:
            if self.hash_table[index].key == key:
                return index
            val = 1
            while self.hash_table[(index + val*val) % self.table_size] is not None:
                if self.hash_table[(index + val*val) % self.table_size].key == key:
                    return (index + val*val) % self.table_size
                val += 1
        return None
        # Returns the index of the hash table entry containing the provided key.
        # If there is not an entry with the provided key, returns None.

    def get_all_keys(self):
        output = []
        for i in self.hash_table:
            if i is not None:
                output.append(i.key)
        return output
        # Returns a Python list of all keys in the hash table.

    def get_value(self, key):
        index = self.get_index(key)
        if index is not None:
            return self.hash_table[index].value
        return None
        # Returns the value (list of line numbers) associated with the key.
        # If key is not in hash table, returns None.

    def get_num_items(self):
        return self.num_items
        # Returns the number of entries (words) in the table.

    def get_table_size(self):
        return self.table_size
        # Returns the size of the hash table.

    def get_load_factor(self):
        return self.num_items/self.table_size
        # Returns the load factor of the hash table (entries / table_size).

