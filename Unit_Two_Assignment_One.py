#
#
#Author: Onyebuchi Iyase
#Program: Multiple 3 and 7
#
#
#
#
#
'''
Program Guide:
        Unit Two - Assignment One 
        Due Wednesday by 11:59pm Points 6 Submitting a file upload Available Feb 8 at 12am - Feb 17 at 11:59pm
        Write a program that prints, line by line, the numbers from 1 to 100.
        For multiples of three print the word “Cow” instead of the number and for the multiples of seven print “Pie” instead of the number.
        For numbers which are multiples of both three and seven print “CowPie"

'''
print('******************************')
print('******************************')
print('  Multiple of three and seven    ')
print("'''''''''''''''''''''''''''''''")
print("'''''''''''''''''''''''''''''''")
for n in range(1, 101):
    if n % 3 == 0 and n % 7 == 0:
        print("CowPie")
    elif n % 3 == 0:
        print("Cow")
    elif n % 7 == 0:
        print("Pie")
    else:
        print(n)
