#
#
#
# Author: Onyebuchi Iyase
# Program: Binary and linear search
#

from mySearches import bsearch, lsearch

'''
Ensure the rands.txt is in the same file directory to open the file
'''
# Open and read the file
with open("rands.txt") as file_rands:
    raw_data = file_rands.read()

# Split the raw data into a list of strings
raw_list = raw_data.split()

# Convert the strings to integers
# using list comprehension to loop through raw_list
data = [int(x) for x in raw_list]

# Sort the data accordingly
data.sort()

# Search for the numbers given numbers: 78700, 3333, and 1118
nums_to_search = [78700, 3333, 1118]

for number in nums_to_search:
    # Binary search at the index and count
    index, count = bsearch(number, data)
    if index == -1:
        print(f"{number} not found. Binary search performed {count} lookups.")
    else:
        print(f"{number} found at index {index}. Binary search performed {count} lookups.")

    # Linear search at the index and count
    index, count = lsearch(number, data)
    if index == -1:
        print(f"{number} not found. Linear search performed {count} lookups.")
    else:
        print(f"{number} found at index {index}. Linear search performed {count} lookups.")
