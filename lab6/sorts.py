import random
import time

# Sorts a list by selecting the minimum number in the list and swapping it with the current index
def selection_sort(list):
    min_index = 0
    comparisons = 0
    # keeps track of the current index "ind" and number "item"  at the index
    for ind, item in enumerate(list):
        # Initially starts with the first item as the minimum
        min = item
        # Searches the rest of the list for the minimum number smaller than the current min
        for index, value in enumerate(list[ind + 1:]):
            comparisons += 1
            # If a smaller value is found, it is stored as the new min
            if value < min:
                min = value
                min_index = index + ind + 1
        # If a new min was found, it is swapped with the current index
        if min != item:
            list[ind] = min
            list[min_index] = item
    return comparisons

# def insertion(list):
#     comparisons = 0
#     num = 0
#     if len(list) == 1 or len(list) == 0:
#         return comparisons
#     else:
#         while num < len(list):
#             index = num
#             while index > 0:
#                 comparisons += 1
#                 if list[index] >= list[index - 1]:
#                     break
#                 else:
#                     num1 = list[index]
#                     num2 = list[index - 1]
#                     list[index] = num2
#                     list[index - 1] = num1
#                     index -= 1
#             num += 1
#     return comparisons

# Inserts an element in the correct spot by swapping it with preceding values in the list if
# the current element is less than the preceding value
def insertion_sort(list):
    comparisons = 0
    num = 0
    # Returns list if its length is 0 or 1
    if len(list) == 1 or len(list) == 0:
        return comparisons
    else:
        # Steps through each item in the list
        for i in list:
            index = num
            # Steps through the preceding values in the list from end to beginning
            while index > 0:
                comparisons += 1
                # If the current number is less than the preceding value, they are swapped
                if i < list[index - 1]:
                    list[index] = list[index - 1]
                    list[index - 1] = i
                    index -= 1
                # If not, move on to the next index
                else:
                    index = 0
            num += 1
    return comparisons
#
# def main():
#     # Give the random number generator a seed, so the same sequence of
#     # random numbers is generated at each run
#     random.seed(1234)
#
#     # Generate 5000 random numbers from 0 to 999,999
#     randoms = random.sample(range(1000000), 4000)
#     start_time = time.time()
#     comps = selection_sort(randoms)
#     stop_time = time.time()
#     print(comps, stop_time - start_time)
#
#     random_nums = random.sample(range(1000000), 4000)
#     start = time.time()
#     compare = insertion_sort(random_nums)
#     stop = time.time()
#     print(compare, stop - start)
#
# if __name__ == '__main__':
#     main()

