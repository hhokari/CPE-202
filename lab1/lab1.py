#
#Emily Gavrilenko
#015218875
#4/5/2019
#
#Lab 0
#Section 12

def max_list_iter(int_list):
   if int_list is None:     #raises ValueError if list is None
      raise ValueError
   elif len(int_list) == 0: #returns None if list is empty
      return None
   max = int_list[0]        #starts off with initial value as the max
   for val in int_list:     #replaces max with a greater number if found later in list
      if val > max:
         max = val
   return max

def reverse_rec(int_list):
   if int_list is None:       #returns ValueError if list is None
      raise ValueError
   elif len(int_list) == 0:   #returns None is list is empty
      return None
   elif (len(int_list) == 1): #return the list if length=1
      return int_list
   else:
      first = [int_list[-1]]  #adds the last number of the list to the front
      return first + reverse_rec(int_list[0:-1]) #repeats excluding the previous last number


def bin_search(target, low, high, int_list):
   mid = (low + high)//2          #finds middle index
   if int_list == None:           #raises ValueError if list is None
      raise ValueError
   if len(int_list) == 0:         #returns None if list is empty
      return None
   if target == int_list[mid]:    #returns index if target is found in the middle
      return mid
   if low > high:                 #return None if target isn't found in the list
      return None
   elif target > int_list[mid]:   #repeats search but only looking at numbers greater than the middle number
      return bin_search(target, mid + 1, high, int_list)
   elif target < int_list[mid]:   #repeats search but only looking at numbers greater than the middle number
      return bin_search(target, low, mid - 1, int_list)



   


