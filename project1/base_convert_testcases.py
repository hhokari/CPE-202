import unittest
from  base_convert import *

class TestBaseConvert(unittest.TestCase):

    def test_base3(self):
        self.assertEqual(convert(12,3), "110")

    def test_base2(self):
        self.assertEqual(convert(45,2),"101101")

    def test_base4(self):
        self.assertEqual(convert(30,4),"132")

    def test_base16(self):
        self.assertEqual(convert(314, 16), "13A")
        self.assertEqual(convert(315, 16), "13B")
        self.assertEqual(convert(316, 16), "13C")
        self.assertEqual(convert(317, 16), "13D")
        self.assertEqual(convert(318, 16), "13E")
        self.assertEqual(convert(319, 16), "13F")
        self.assertEqual(convert(11259375, 16), "ABCDEF")

    def test_base10(self):
        self.assertEqual(convert(0, 10), "0")
        self.assertEqual(convert(1,10),"1")



if __name__ == "__main__":
        unittest.main()