#
# Emily Gavrilenko
# 015218875
# 4/11/2019
#
# Lab 0
# Section 12
#This program returns True if it's possible to win the bear game starting with n bears, and False otherwise

def bears(n):
    #checks to see if n is an integer; if not, returns False
    try:
        int(n)
    except ValueError:
        return False
    if n == 42:
        return True
    #if n is equal to 42, return True

    if n > 42:
        if n%2 == 0:
        #if n is even, gives back n/2 bears
            if bears(int(n/2)) is True:
                #returns True if giving back n/2 bears ultimately results in 42 bears
                return True

        if n%5 == 0:
        #if n is divisible by 5, gives back 42 bears
            if bears(int(n-42)) is True:
                # returns True if giving back 42 bears ultimately results in 42 bears
                return True

        if n % 3 == 0 or n % 4 == 0:
            #if n is divisible by 3 or 4, gives back num bears
            val = list(str(n))
            num = int(val[-1]) * int(val[-2])
            # num is the last two digits of n multiplied by each other
            if num == 0:
                #returns false if n is zero because the same n will be passed forever otherwise
                return False
            if bears(n-num) is True:
                # returns True if giving back num bears ultimately results in 42 bears
                return True

    return False
    #returns false if there's no way to have 42 bears
