#
# Emily Gavrilenko
# 015218875
# 4/11/2019
#
# Lab 0
# Section 12
#This program converts the input number num in base 10 to its equivalent value in base b

def convert(num, b):
    # finds the quotient and remainder
    quotient = num // b
    remainder = num % b

    # bases 10-15 are replaced with the symbols A-F
    if remainder == 10:
        remainder = "A"
    if remainder == 11:
        remainder = "B"
    if remainder == 12:
        remainder = "C"
    if remainder == 13:
        remainder = "D"
    if remainder == 14:
        remainder = "E"
    if remainder == 15:
        remainder = "F"

    # stops recursion when the quotient reaches 0
    if quotient == 0:
        return str(remainder)

    # returns a string representing the conversion of num to base b
    return str(convert(quotient, b)) + str(remainder)
