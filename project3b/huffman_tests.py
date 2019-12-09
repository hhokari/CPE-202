#
#Emily Gavrilenko
#015218875
#5/14/2019
#
#Lab 0
#Section 12

import unittest
import filecmp
import subprocess
from huffman import *

usediff = False
class TestList(unittest.TestCase):
    def test_cnt_freq(self):
        freqlist = cnt_freq("file2.txt")
        anslist = [2, 4, 8, 16, 0, 2, 0]
        self.assertListEqual(freqlist[97:104], anslist)

    def test_create_huff_tree(self):
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        self.assertEqual(hufftree.freq, 32)
        self.assertEqual(hufftree.char, 97)
        left = hufftree.left
        self.assertEqual(left.freq, 16)
        self.assertEqual(left.char, 97)
        right = hufftree.right
        self.assertEqual(right.freq, 16)
        self.assertEqual(right.char, 100)

    def test_create_header(self):
        freqlist = cnt_freq("file2.txt")
        self.assertEqual(create_header(freqlist), "97 2 98 4 99 8 100 16 102 2")

    def test_create_code(self):
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord('d')], '1')
        self.assertEqual(codes[ord('a')], '0000')
        self.assertEqual(codes[ord('f')], '0001')

    def test_01_textfile(self):
        huffman_encode("file1.txt", "file1_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        if usediff is True:
            err = subprocess.call("diff -wb file1_out.txt file1_soln.txt", shell = True)
            self.assertEqual(err, 0)
        else:
            self.assertTrue(filecmp.cmp("file1_out.txt", "file1_soln.txt"))

    def test_02_textfile(self):
        huffman_encode("file2.txt", "file2_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        if usediff:
            err = subprocess.call("diff -wb file2_out.txt file2_soln.txt", shell = True)
            self.assertEqual(err, 0)
        else:
            self.assertTrue(filecmp.cmp("file2_out.txt", "file2_soln.txt"))

    def test_03_textfile(self):
        huffman_encode("multiline.txt", "multiline_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        if usediff:
            err = subprocess.call("diff -wb multiline_out.txt multiline_soln.txt", shell = True)
            self.assertEqual(err, 0)
        else:
            self.assertTrue(filecmp.cmp("multiline_out.txt", "multiline_soln.txt"))

    def test_04_textfile(self):
        huffman_encode("declaration.txt", "declaration_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        if usediff:
            err = subprocess.call("diff -wb declaration_out.txt declaration_soln.txt", shell = True)
            self.assertEqual(err, 0)
        else:
            self.assertTrue(filecmp.cmp("declaration_out.txt", "declaration_soln.txt"))

    # def test_05_textfile(self):
    #     url_to_text("http://users.csc.calpoly.edu/~grader-ph/202/projects/p3/file_WAP.txt", "warandpeace.txt")
    #     huffman_encode("warandpeace.txt", "warandpeace_out.txt")

    def test_05(self):
        create_new_text("repeated_a.txt", "aaaa")
        huffman_encode("repeated_a.txt", "repeated_a_out.txt")

    def test_06(self):
        create_new_text("empty.txt", "")
        huffman_encode("empty.txt", "empty_out.txt")

    def test_07(self):
        with self.assertRaises(FileNotFoundError):
            huffman_encode("emily.txt", "emily_out.txt")

    def test_decode_1(self):
        huffman_decode("file1_out.txt", "file1_text.txt")
        if usediff is True:
            err = subprocess.call("diff -wb file1.txt file1_text.txt", shell = True)
            self.assertEqual(err, 0)
        else:
            self.assertTrue(filecmp.cmp("file1.txt", "file1_text.txt"))

    def test_decode_2(self):
        huffman_decode("file2_out.txt", "file2_text.txt")
        if usediff is True:
            err = subprocess.call("diff -wb file2.txt file2_text.txt", shell=True)
            self.assertEqual(err, 0)
        else:
            self.assertTrue(filecmp.cmp("file2.txt", "file2_text.txt"))

    def test_decode_3(self):
        huffman_decode("multiline_out.txt", "multiline_text.txt")
        if usediff is True:
            err = subprocess.call("diff -wb multiline.txt multiline_text.txt", shell=True)
            self.assertEqual(err, 0)
        else:
            self.assertTrue(filecmp.cmp("multiline.txt", "multiline_text.txt"))

    def test_decode_4(self):
        huffman_decode("declaration_out.txt", "declaration_text.txt")
        if usediff is True:
            err = subprocess.call("diff -wb declaration.txt declaration_text.txt", shell=True)
            self.assertEqual(err, 0)
        else:
            self.assertTrue(filecmp.cmp("declaration.txt", "declaration_text.txt"))

    def test_decode_5(self):
        huffman_decode("warandpeace_out.txt", "warandpeace_text.txt")
        if usediff is True:
            err = subprocess.call("diff -wb warandpeace.txt warandpeace_text.txt", shell=True)
            self.assertEqual(err, 0)
        else:
            self.assertTrue(filecmp.cmp("warandpeace.txt", "warandpeace_text.txt"))

    def test_decode_6(self):
        huffman_decode("repeated_a_out.txt", "repeated_a_text.txt")
        if usediff is True:
            err = subprocess.call("diff -wb repeated_a.txt repeated_a_text.txt", shell=True)
            self.assertEqual(err, 0)
        else:
            self.assertTrue(filecmp.cmp("repeated_a.txt", "repeated_a_text.txt"))


    def test_decode_7(self):
        huffman_decode("empty_out.txt", "empty_text.txt")
        if usediff is True:
            err = subprocess.call("diff -wb empty.txt empty_text.txt", shell=True)
            self.assertEqual(err, 0)
        else:
            self.assertTrue(filecmp.cmp("empty.txt", "empty_text.txt"))

if __name__ == '__main__':
   unittest.main()
