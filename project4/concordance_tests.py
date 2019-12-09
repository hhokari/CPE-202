#
#Emily Gavrilenko
#015218875
#6/4/2019
#
#Project 4
#Section 12

import unittest
import filecmp
from concordance import *

class TestList(unittest.TestCase):

    def test_0(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")

    def test_00(self):
        conc = Concordance()
        with self.assertRaises(FileNotFoundError):
            conc.load_stop_table("emily.txt")

    def test_01(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("file1.txt")
        conc.write_concordance("file1_con.txt")
        self.assertTrue(filecmp.cmp("file1_con.txt", "file1_sol.txt"))

    def test_02(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("file2.txt")
        conc.write_concordance("file2_con.txt")
        self.assertTrue(filecmp.cmp("file2_con.txt", "file2_sol.txt"))

    def test_03(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("declaration.txt")
        conc.write_concordance("declaration_con.txt")
        self.assertTrue(filecmp.cmp("declaration_con.txt", "declaration_sol.txt"))

    def test_04(self):
        conc =  Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("stop_words.txt")
        conc.write_concordance("stop_empty.txt")

    def test_05(self):
        conc = Concordance()
        conc.create_new_text("test.txt", "Hello this is a test hello hopefully this test works hello")
        conc.load_stop_table("stop_empty.txt")
        conc.load_concordance_table("test.txt")
        conc.write_concordance("test_output.txt")

if __name__ == '__main__':
   unittest.main()
