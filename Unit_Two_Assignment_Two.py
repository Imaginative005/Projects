#
#
#
#
#Author: Onyebuchi Iyase
#Program: Average negative numbers
#

print('******************************')
print('******************************')
print('  Average Negative numbers     ')
print("'''''''''''''''''''''''''''''''")
print("'''''''''''''''''''''''''''''''")



'''
Program Guide:

            Unit Two - Assignment Two 
            Due Wednesday by 11:59pm Points 6 Submitting a file upload Available Feb 9 at 12am - Feb 17 at 11:59pm
            MyList = [ 23, -45, 6, -23, -9, 77, 54, -54, 21, -2, 8, -3, -23, 45, 93, -43, 999, -2, 3, 78, 90 ]

            Given the list above, write a program that prints out the average of the negative numbers in the
            list that appear before a 999 is detected.  

'''


#Using the given hard coded list
MyList = [ 23, -45, 6, -23, -9, 77, 54, -54, 21, -2, 8, -3, -23, 45, 93, -43, 999, -2, 3, 78, 90 ]
store_negative_numbers = []
for number in MyList:
    if number < 0:
        store_negative_numbers.append(number)
average = sum(store_negative_numbers) / float(len(store_negative_numbers))
length_of_negative_numbers = len(store_negative_numbers)
#average_negative_numbers = store_negative_numbers / length_of_negative_numbers

print(f'The numbers in MyList: {MyList}')
print(f'The length of the negative numbers: {length_of_negative_numbers}')
print(f'All the negative numbers in MyList: {store_negative_numbers}')
print(f'The average of the negative numbers in MyList: { average}')

#to two decimal place
#print(f'The rounded average negative numbers in MyList: {round(average, 2)}')

#To whole a number
#print(f'The rounded average negative numbers in MyList: {round(average)}')

 


'''
#Method 2: For Testing purpose for random generated numbers from -999 to 1000 excluding 1000
#Rmove the doctring to run at the top and bottom, but don't run the two method at the same time
import random
#random_numbers = random.randint(-999, 999)
random_list = []
for number in range(-999, 1000):
    if number < 0:
        random_list.append(number)
print(random_list)

average_generated_numbers = sum(random_list) / float(len(random_list))
print(f'The average random generated numbers are: {average_generated_numbers}')

'''
