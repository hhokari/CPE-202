#
# Emily Gavrilenko
# 015218875
# 6/4/2019
#
# Project 4
# Section 12

from hash_quad import *
import string

class Concordance:

    def __init__(self):
        self.stop_table = None          # hash table for stop words
        self.concordance_table = None   # hash table for concordance

    # Removes punctuation and digits from the file line
    def remove(self, value):
        result = ""
        for c in value:
            # If char is not punctuation, add it to the result.
            if c not in string.punctuation:
                if c not in string.digits:
                    result += c
        return result

    # Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
    # If file does not exist, raise FileNotFoundError
    def load_stop_table(self, filename):
        new_file = open(filename, "r")
        line = new_file.readline()
        self.stop_table = HashTable(191)
        while line != "":
            list = line.split()
            self.stop_table.insert(list[0], 0)
            line = new_file.readline()
        new_file.close()

    # Read words from input text file (filename) and insert them into the concordance hash table,
    # after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
    # Does not include duplicate line numbers (word appearing on same line more than once)
    # If file does not exist, raise FileNotFoundError
    def load_concordance_table(self, filename):
        file = open(filename, "r")
        line_num = 1
        line = file.readline()
        self.concordance_table = HashTable(191)
        while line != "":
            # Splits words between a hyphen into two seperate words
            new_line = line.replace("-", " ")
            # Removes all punctuation and digits
            removed = self.remove(new_line)
            word_list = removed.split()
            for i in word_list:
                i = i.lower()
                # Adds all words not in the stop_table to the concordance table
                if self.stop_table.in_table(i) is False:
                    self.concordance_table.insert(i, line_num)
            line = file.readline()
            line_num += 1
        file.close()


    # Write the concordance entries to the output file(filename)
    def write_concordance(self, filename):
        file = open(filename, "w+", newline="")
        list = []
        # Adds all not None entries of the concordance hash table to list
        for i in self.concordance_table.hash_table:
            if i is not None:
                list.append(i)
        # Sorts the list in alphabetical order
        newlist = sorted(list, key=lambda x: x.key)
        for i in newlist[:len(newlist)-1]:
            key = i.key
            location = i.value
            # Creates a string out of the list of line numbers
            occur = " ".join(str(x) for x in location)
            # Creates a string of the key and line occurences
            file.write(key + ": " + occur + "\n")
        if newlist != []:
            # Adds the last word to the end of the file without a newline afterwards
            key = newlist[-1].key
            location = newlist[-1].value
            occur = " ".join(str(x) for x in location)
            file.write(key + ": " + occur)
        file.close()

    # Creates an new text file
    def create_new_text(self, out_file, text):
        new_file = open(out_file, "w+", newline="")
        new_file.write(text)
        new_file.close()

