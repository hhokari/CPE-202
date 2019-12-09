#
#Emily Gavrilenko
#015218875
#4/11/2019
#
#Lab 0
#Section 12
#This program outputs a list containing all the possible permutations of an input string

def perm_gen_lex(a):
    test = []
    #test is an empty list that will contain all the permutations at the end
    if len(a) == 0:
        return list(a)
    if len(a) == 1:
        return list(a)
    else:
        for i in range(len(a)):
            #goes through every character in the string
            num = a[i]
            b = a.replace(num, '', 1)
            #removes the letter at index i to form a simpler string
            if len(b) == 1:
                #stops permutating when the length of the string is one
                value = ''.join([num] + [b])
                #adds the removed value to the front of the remaining string
                if test.count(value) == 0:
                    test.append(value)
                #adds the permutation to the outputed list if it hasn't been added already
            else:
                for i in perm_gen_lex(b):
                    #goes through every index in the permutation
                    perm = ''.join([num] + [i])
                    #adds the removed value to the front of the remaining string
                    if test.count(perm) == 0:
                        test.append(perm)
                    #adds the permutations to the outputed list
    return test
    #returns the list with all the possible permutations
