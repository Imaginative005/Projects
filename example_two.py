

# Creating the main program mainProg.py:

import myLib

# Opening the input file Rumbers.txt
with open('Rumbers.txt', 'r') as infile:
    # Reading the contents of the file into a list
    nums = infile.readlines()

# Converting each element in the list to an integer and storing them in a 2D list
nums = [[int(num) for num in row.split('\t')] for row in nums]

# Initializing the sum of Harshad numbers and the list of Harshad numbers with '7' in their second column
harshad_sum = 0
harshad_seven = []

# Looping through each number in the list
for row in nums:
    for num in row:
        # Checking if the number is Harshad
        if myLib.isHarshad(num):
            # Incrementing the sum of Harshad numbers
            harshad_sum += num
            # Checking if the number has '7' in its second column
            if myLib.isSiete(num):
                # Checking if the number is divisible by Hodges
                if num % myLib.Hodges == 0:
                    # Adding the number to the list of Harshad numbers with '7' in their second column
                    harshad_seven.append(num)

# Printing the sum of Harshad numbers
print("Sum of Harshad numbers:", harshad_sum)

# Printing the Harshad numbers with '7' in their second column and are divisible by Hodges
print("Harshad numbers with '7' in second column and divisible by Hodges:")
for num in harshad_seven:
    print(num)

# Writing the Harshad numbers with '7' in their second column to the output file HarshOut.txt
with open('HarshOut.txt', 'w') as outfile:
    for num in harshad_seven:
        outfile.write(str(num) + '\n')

# Closing the input and output files
infile.close()
outfile.close()

