#
#
#Author: Onyebuchi Iyase
#Program: Harshad number
#
#
#
#
#

'''
Program Guide:

    A Harshad number (or a Niven number) is a number that is evenly divisible by the sum of its digits.
    An example is 18 (1+8=9, 18%9 = 0) or 270 (2+7+0=9, 270%9 = 0). 

    Write a function called isHarshad(num) that takes an integer as an argument
    and returns True if the number is a Harshad number and False if it is not.
    Then, use this function to create a list of all of
    the Harshad numbers in the first 500 natural numbers.
'''
#logic breakdown
#individual number digit is added,
#use the result of the sum as the module
#if the remainder is zero return true
#using sum(map(int, str(number))) works as well

number = int(input("Enter the number you want to check: "))
'''
def isHarshad(number):
    num = sum(int(n) for n in str(number))
    #print(num)
    for i in range(1, 501):
        if number % num == 0:
            return True
        else:
            return False
'''
#updated version
def isHarshad(num):
    if num == 0:
        return False
    else:
        sum_digits = sum([int(digit) for digit in str(num)])
        return num % sum_digits == 0
# using list comprehension and to test
#harshad_numbers = [number for number in range(1, 501) if isHarshad(number)]
print(f"{number} is {isHarshad(number)}")
#print(f"The list of all harshad number in the first 500 natural numbers: {harshad_numbers}")
