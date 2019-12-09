#
#Emily Gavrilenko
#015218875
#4/23/2019
#
#Project2
#Section 12

import unittest
from exp_eval import *

class test_expressions(unittest.TestCase):
    def test_postfix_eval(self):
        self.assertAlmostEqual(postfix_eval("5 1 2 + 4 ** + 3 -"), 83)

    def test_postfix_eval_01(self):
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)

    def test_postfix_eval_02(self):
        try:
            postfix_eval("blah")
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_Invalid_token(self):
        try:
            postfix_eval("3 5 + blah")
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_Insufficient_operands(self):
        try:
            postfix_eval("+")
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")
        try:
            postfix_eval("2 >>")
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_03(self):
        try:
            postfix_eval("4 +")
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_04(self):
        try:
            postfix_eval("1 2 3 +")
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")

    def test_postfix_eval_05(self):
        self.assertAlmostEqual(postfix_eval("6 4 3 + 2 - * 6 /"), 5)

    def test_postfix_eval_06(self):
        self.assertAlmostEqual(postfix_eval("1 2 3 ** + 1 << 10 1 >> +"), 23)

    def test_postfix_eval_07(self):
        self.assertAlmostEqual(postfix_eval("12"), 12)

    def test_postfix_eval_08(self):
        self.assertAlmostEqual(postfix_eval("12.0"), 12.0)

    def test_postfix_eval_09(self):
        self.assertAlmostEqual(postfix_eval("7 2 + 4 / 3 -"), -0.75)

    def test_postfix_eval_10(self):
        self.assertAlmostEqual(postfix_eval("1.0 2.0 3.0 ** + 1 << 10 1 >> +"), 23)

    def test_postfix_eval_11(self):
        self.assertAlmostEqual(postfix_eval("1.1 4.5 + 4.7 * 2.1 /"), 12.5333333333)

    def test_postfix_eval_0_divisor(self):
        with self.assertRaises(ValueError):
            postfix_eval("2 0 /")

    def test_postfix_eval_illegal_bit_shift(self):
        try:
            postfix_eval("5 2 / 1 <<")
        except PostfixFormatException as e:
            print("error")
            self.assertEqual(str(e), "Illegal bit shift operand")

    def test_infix_to_postfix_01(self):
        self.assertEqual(infix_to_postfix("3.3 - 7 * 2.2"), "3.3 7 2.2 * -")
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")
        self.assertEqual(infix_to_postfix("6"), "6")
        self.assertEqual(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 ) ** 2 ** 3"), "3 4 2 * 1 5 - 2 3 ** ** / +")
        self.assertEqual(infix_to_postfix("5 - 1 + ( 2 + 3 )"), "5 1 - 2 3 + +")
        self.assertEqual(infix_to_postfix("5 * ( 6 + 3 - 7 * 3 + 2 ) / 6"), "5 6 3 + 7 3 * - 2 + * 6 /")
        self.assertEqual(infix_to_postfix("8 + 3 * 4 + ( 6 - 2 + 2 * ( 6 / 3 - 1 ) - 3 )"), "8 3 4 * + 6 2 - 2 6 3 / 1 - * + 3 - +")
        self.assertEqual(infix_to_postfix("2 >> 1 << 1 ** 3"), "2 1 >> 1 << 3 **")

    def test_prefix_to_postfix(self):
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")
        self.assertEqual(prefix_to_postfix("- 5 * 6 7"), "5 6 7 * -")
        self.assertEqual(prefix_to_postfix("+ + + 5 -7.1 11 3"), "5 -7.1 + 11 + 3 +")

if __name__ == "__main__":
    unittest.main()
