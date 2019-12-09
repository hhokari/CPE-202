#
#Emily Gavrilenko
#015218875
#5/14/2019
#
#Lab 0
#Section 12
import urllib.request
import shutil

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char   # stored as an integer - the ASCII character code value
        self.freq = freq   # the freqency associated with the node
        self.left = None   # Huffman tree (node) to the left
        self.right = None  # Huffman tree (node) to the right

# Returns True if tree rooted at node a comes before tree rooted at node b, False otherwise
def comes_before(a, b):
    # Returns True if the frequency of a is lower than the frequency of b
    if int(a.freq) < int(b.freq):
        return True
    # Returns True is the ASCII value of character a is less than that of b
    if int(a.freq) == int(b.freq):
        if a.char < b.char:
            return True
    return False

# Creates and returns a new Huffman node with children a and b, with the "lesser node" on the left
# The new node's frequency value will be the sum of the a and b frequencies
# The new node's char value will be the lesser of the a and b char ASCII values
def combine(a, b):
    parent_node = HuffmanNode(find_min(a,b), int(a.freq) + int(b.freq))
    parent_node.left = a
    parent_node.right = b
    return parent_node

# Finds the character with the lower ASCII value to be displayed in the parent node
def find_min(a,b):
    ord_a = a.char
    ord_b = b.char
    if ord_a < ord_b:
        return a.char
    if ord_b < ord_a:
        return b.char


# Opens a text file with a given file name (passed as a string) and counts the
# frequency of occurrences of all the characters within that file
def cnt_freq(filename):
    f = open(filename, "r")
    items = f.read()
    file = list(items)
    output_list = [0]*256
    f.close()
    for i in file:
        val = output_list[ord(i)]
        output_list[ord(i)] = val +1
    return output_list

# Creates a Huffman tree for characters with non-zero frequency
# Returns the root node of the Huffman tree
def create_huff_tree(char_freq):
    index = 0
    sorted_list = []
    # Creates a HuffmanNode for each character present in the file
    # Creates a sorted list of all the created nodes
    for i in char_freq:
        if i != 0:
            node = HuffmanNode(index, i)
            sorted_list = add_to_sorted_list(node, sorted_list)
        index += 1

    # Combines the sorted nodes into a binary tree with lower frequencies on the bottom
    # and higher frequencies on the top
    while len(sorted_list) > 1:
        new_node = combine(sorted_list[0], sorted_list[1])
        sorted_list = add_to_sorted_list(new_node, sorted_list[2:])

    # Returns the root of the binary tree of ordered HuffmanNodes
    return sorted_list[0]

# Adds a node to its correct spot in the sorted node list
def add_to_sorted_list(node, sorted_list):
    if len(sorted_list) == 0:
        sorted_list.append(node)
    else:
        ind = 0
        for i in sorted_list:
            if comes_before(node, i) is True:
                sorted_list.insert(ind, node)
                break
            ind += 1
        if comes_before(node, sorted_list[-1]) is False:
            sorted_list.append(node)
    return sorted_list

# Traverses the Huffman tree that was passed
# Returns an array (using a Python list) of 256 strings
# Use the character’s respective integer ASCII representation as the index into the array
# The resulting Huffman code for that character is stored at that location.
# Traverse the tree from the root to each leaf node and
# Add a ’0’ when we go ’left’ and a ’1’ when we go ’right’ constructing a string of 0’s and 1’s.
def create_code(node):
    if node.left is None and node.right is None:
        return []
    code_list = ['']*256
    code = []
    return create_code_helper(node, code, code_list)


def create_code_helper(node, code, list):
    if node.left is not None:
        # Adds a zero when going left
        code_left = code + [0]
        val = convert(code_left)
        # Creates a unique string of 1s and 0s for the unique tree node
        # Adds to the index of the array according to the character’s respective integer ASCII representation
        list[node.left.char] = val
        list = create_code_helper(node.left, code_left, list)
    if node.right is not None:
        # Adds a one when going right
        code_right = code + [1]
        val = convert(code_right)
        list[node.right.char] = val
        # Creates a unique string of 1s and 0s for the unique tree node
        # Adds to the index of the array according to the character’s respective integer ASCII representation
        list = create_code_helper(node.right, code_right, list)
    return list

# Converts a list of 0 and 1 values into a single value
def convert(list):
    # Converting integer list to string list
    s = [str(i) for i in list]
    # Join list items using join()
    result = "".join(s)
    return result


# Input is the list of frequencies.
# Creates and returns a header for the output file
# Output is the list of ASCII values of the characters followed by their frequencies
def create_header(freqs):
    list = []
    index = 0
    for i in freqs:
        if i != 0:
            list.append(str(index))
            list.append(str(i))
        index += 1
    output = " ".join(list)
    return output


# Takes a file of characters and a code of 0 and 1 values for every character in a binary tree
# Returns a string of 0s and 1s defining the route needed to recreate the file of characters
# By traversing the binary tree
def create_output_code(file, array_code):
    # Opens file and saves each individual character in "items"
    f = open(file, "r")
    contents = f.read()
    items = list(contents)
    item_list = []
    # Finds the corresponding code for traversing the binary tree for each character in the file
    # Combines all the codes and returns it as the string "joined"
    for i in items:
        val = array_code[ord(i)]
        item_list.append(val)
    joined = ''.join(item_list)
    f.close()
    return joined


# Takes inout file name and output file name as parameters
# Uses the Huffman coding process on the text from the input file and writes encoded text to output file
# Take note of special cases - empty file and file with only one unique character
def huffman_encode(in_file, out_file):
    # Creates a header for the file using the methods cnt_freq and create_header
    frequency = cnt_freq(in_file)
    header = create_header(frequency)
    # Creates an empty file if the input is an empty file
    if header is "":
        new_file = open(out_file, "w+", newline="")
        new_file.close()
        return new_file
    # Opens out_file and adds the header to the file
    new_file = open(out_file, "w+", newline="")
    new_file.write(header)
    # Creates a binary tree for the file and an array of codes for each character in the file
    root = create_huff_tree(frequency)
    codes = create_code(root)
    if codes != []:
        # Creates a code of 0s and 1s for the traversal of the binary tree for each character in the file
        test = create_output_code(in_file, codes)
        # Adds the code to the file if there's more than one characters in the file
        new_file.write("\n")
        new_file.write(test)
    new_file.close()

def create_new_text(out_file, text):
    new_file = open(out_file, "w+", newline="")
    new_file.write(text)
    new_file.close()

# Creates an output list identical to the cnt_freq list from an encoded file header
def parse_header(header_string):
    # Creates a list splitting up all the numbers as a single entry in the list
    header = header_string.split()
    index = 0
    freq_list = [0]*256
    # Steps through all the numbers in the header
    for i in header:
        # If the number is at an even index (contains the ASCII value)
        # Stores that value as "a"
        if index%2 == 0:
            a = int(i)
            index +=1
        # If the number is at an odd index (contains the number of occurrences of a)
        # Stores the number at index "a"
        else:
            freq_list[a] = i
            index += 1
    return freq_list

# Takes inout file name and output file name as parameters
# Uses the Huffman coding process on the code of 1s and 0s to parse through the huffman tree
# And returns the character found at the leaf nodes to recreate the original test file
# Take note of special cases - empty file and file with only one unique character
def huffman_decode(encoded_file, decode_file):
    new_file = open(encoded_file, "r")
    # Reads the header as the first line in the encoded file
    header = new_file.readline()
    # If the header is empty, the text file is empty and an empty file is returned
    if header is "":
        edit = open(decode_file, "w+", newline="")
        edit.close()
        new_file.close()
        return new_file
    # Reads the 1s and 0s of the encoded file one at a time
    code = new_file.read(1)
    if code is "":
        list = header.split()
        edit = open(decode_file, "w+", newline="")
        output = [chr(int(list[0]))]*int(list[1])
        final = ''.join(output)
        edit.write(final)
        edit.close()
        new_file.close()
        return new_file

    # Creates a frequency list identical to the list returned in the function cnt_freq
    frequency = parse_header(header)
    # Creates a huffman tree and saves the root of it as "root"
    root = create_huff_tree(frequency)
    # Begins traversing the tree at the root
    node = root
    # Opens the output text file
    edit = open(decode_file, "w+", newline="")
    # While there is still code to read in the file
    while code == "0" or code == "1":
        # Goes left in the huffman tree for 0s
        if code == '0':
            node = node.left
        # Goes right in the huffman tree for 1s
        if code == '1':
            node = node.right
        # Adds the character to the output test file if at a leaf node
        if node.left is None and node.right is None:
            edit.write(chr(node.char))
            node = root
        # Reads the next number in the encoded file
        code = new_file.read(1)
    new_file.close()
    edit.close()
    return decode_file

# Returns a text file containing the text of an imput url
# def url_to_text(url, file_name):
#     page = urllib.request.urlopen(url)
#     f = open(file_name, "wb")
#     shutil.copyfileobj(page, f)
#     f.close()




