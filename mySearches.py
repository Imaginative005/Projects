# Conduct a binary search for x in lst
'''
first and last number
continue to check if the middle number is the current number
if the middle is less then moves forward and return the middle and the count
else moves backward
'''


def bsearch(x, lst):
    low = 0
    high = len(lst) - 1
    count = 0

    while low <= high:
        mid = (low + high) // 2
        count += 1
        if lst[mid] == x:
            return mid, count
        elif lst[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1, count


# Conduct a linear search for x in lst.
'''
loop through the list of the list
checking if the current number in the loop
is the same as the current number withing the loop
if true returns the current number and the count
else return -1, count
'''


def lsearch(x, lst):
    count = 0

    for i in range(len(lst)):
        count += 1
        if lst[i] == x:
            return i, count

    return -1, count
