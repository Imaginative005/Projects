#Here's a solution to the problem using Python:

#Step 1: Create a file named "myLib.py" with the following contents:

# myLib.py

def isHarshad(num):
    if num == 0:
        return False
    else:
        sum_digits = sum([int(digit) for digit in str(num)])
        return num % sum_digits == 0

def isSiete(num):
    num_str = str(num)
    if len(num_str) < 2:
        return False
    else:
        return num_str[1] == '7'

Hodges = 14
#The isHarshad() function takes an integer as input and returns True if it is a Harshad number and False otherwise. 
# The isSiete() function takes an integer as input and returns True if its second digit is a '7' and False otherwise. The Hodges constant is set to 14.

#Step 2: Create a file named "mainProg.py" with the following contents:


# mainProg.py

from myLib import isHarshad, isSiete, Hodges

# Open Rumbers.txt
with open('Rumbers.txt', 'r') as infile:
    lines = infile.readlines()

# Deliverable #1: Sum of Harshad numbers
harshad_sum = 0
# Deliverable #2: Harshad numbers with a '7' in the second digit
harshad_siete_list = []
# Deliverable #3: Harshad numbers with a '7' in the second digit and divisible by Hodges
harshad_siete_hodges_count = 0

# Process the lines
for line in lines:
    numbers = line.strip().split('\t')
    for num in numbers:
        num = int(num)
        if isHarshad(num):
            harshad_sum += num
            if isSiete(num):
                harshad_siete_list.append(num)
                if num % Hodges == 0:
                    harshad_siete_hodges_count += 1

# Print the sum of Harshad numbers and the Harshad numbers with a '7' in the second digit and divisible by Hodges
print(f"Sum of Harshad numbers: {harshad_sum}")
print(f"Harshad numbers with a '7' in the second digit and divisible by Hodges: {harshad_siete_hodges_count}")

# Write the Harshad numbers with a '7' in the second digit to HarshOut.txt
with open('HarshOut.txt', 'w') as outfile:
    for num in harshad_siete_list:
        outfile.write(f"{num}\n")
#The main program imports the isHarshad(), isSiete(), and Hodges constant from the "myLib.py" file. It then reads in the "Rumbers.txt" file and processes each number, checking whether it is a Harshad number and whether it has a '7' in the second digit. The sum of Harshad numbers is accumulated and the Harshad numbers with a '7' in the second digit are stored in a list. The program also counts the number of Harshad numbers with a '7' in the second digit that are divisible by the Hodges constant. Finally, the program prints the sum of Harshad numbers and the count of Harshad numbers with a '7' in the second digit that are divisible by Hodges, and writes the Harshad numbers with a '7



