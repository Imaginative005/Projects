#
#
#
#
#Author: Onyebuchi Iyase
#
#Program: Guessing Game: 
#
#
#         Method 1: Harded Coded Predefined age, weight. Used for loop to ask the user to guess the age and weight
#                   While loop to keep the game running and for loop to run the game within the range of the predefined age and weight
#                   Remove comments to run the random generated age, weight and import random statement

#
#         These parts are for self testing, not included for grading purpose:
#
#                   Uncomment to see each other methods result, don't run the methods at the same time
#                   Method 2: Predefined the age, random generated, if the age and weight matches the predefined, the user got it correct
#
#                  

'''
Unit One - Assignment Two 
Program Guide:
            Create a program in Python that stores an age and a weight (just set up two hard coded variables) and allow the user to try to guess your two numbers. 

            Once the user’s two guesses are input your program must behave in the following way:

            If both guesses are higher than the two numbers, print “Both Higher”
            If both guesses are lower than the two numbers, print “Both Lower”
            if both numbers are guessed correctly print “Bingo”
            and lastly, if none of the three conditions above is true print “Game Over”
Example (25 and 135 are the numbers):

 

Enter your guess for age: 27

Enter your guess for weight: 200

Both Higher

 

Enter your guess for age: 2

Enter your guess for weight: 800

Game Over

 

Enter your guess for age: 25

Enter your guess for weight: 135

Bingo

 

Enter your guess for age: 800

Enter your guess for weight: 2

Game Over

 

Enter your guess for age: 0

Enter your guess for weight: 9

Both Lower


Note that for every pair of guesses, we will have to run the program again. 


'''

print('*******************')
print('*******************')
print('Welcome to Guessing Game')
print("''''''''''''''''''''''''")
print("''''''''''''''''''''''''")


#Method 1: Using for loop, for submission
age = 25
weight = 135
'''
#To test for random age and weight, remove the comment for random genearated age & weight
import random
age = random.randint(3, 120)
weight = random.randint(30, 300)
#Test to see the answer while testing, comment to hid the answer for the user
print(f"The correct age is: {age} and weight: {weight}")
'''
game_is_on = True
while game_is_on:
    for number in range(age, weight):
        user_age = int(input("Enter your guess for age: "))
        user_weight = int(input("Enter your guess for weight: "))
        if user_age > age and user_weight > weight:
            print("Both higher")
        elif user_age < age and user_weight < weight:
            print("Both lower")
        elif user_age == age and user_weight == weight:
            print("Bingo")
        else:
            print("Game Over")
            game_is_on = False
            
    

    
        
'''
#Method 2: Hard coded age, and random generated
#Predefined the age and weight, if the age and weight matches the predefined, the user got it correct, Bingo!
#age = 25
#weight = 135
import random

age = random.randint(3, 120)
weight = random.randint(30, 300)
#Shows the answer for testing
print(f"The correct answer: age is {age} and weight is {weight}")
game_attempts = 5
print(f"You have {game_attempts} attempts for this game")
#def game_attempts_remain(number):
 #   number -= 1
  #     return f"Game Over! {number} remaining"
game_is_on = True
while game_is_on:
    user_age_guess = int(input("Enter your guess for age: "))
    user_weight_guess = int(input("Enter your guess for weight: "))
    #Test case when the age and weight are both high
    if user_age_guess > age and user_weight_guess > weight:
        game_attempts -= 1
        if game_attempts == 0:
            game_is_one = False
            print("Game Over")
        print(f"Both Higher! You have {game_attempts} attempts remaining.")
    #Test case when the age and weight are  both lower
    elif user_age_guess < age and user_weight_guess < weight:
        game_attempts -= 1
        if game_attempts == 0:
            game_is_on = False
            print("Game Over")
        print(f"Both Lower! You have {game_attempts} attempts remaining")
       
        #This condition run if the user guess age is greater and the weight is lower
    elif user_age_guess > age and user_weight_guess < weight:
        game_attempts -= 1
        if game_attempts == 0:
            game_is_on = False
            print("Game Over")
        print(f"The age {user_age_guess} is higher but the {user_weight_guess} weight is lower. \nYou have {game_attempts} attempts remaining. Try again!")
        #This condition runs if the user guess age is lower and the weight is higher
    elif user_age_guess < age and user_weight_guess > weight:
        game_attempts -= 1
        if game_attempts == 0:
            game_is_on = False
            print("Game Over")
        print(f"The age {user_age_guess} is lower but the {user_weight_guess} weight is higher. \nYou have {game_attempts} attempts remaining. Try again!")
        #Test when the user guess both age and weight correctly, the game ends
    elif user_age_guess == age and user_weight_guess == weight:
        game_is_on = False
        print("Bingo")
        #Test when the user didn't guess the correct age and weight and attempt is 0
    elif user_age_guess > age and user_weight_guess > weight and game_attempts == 0:
        game_is_on = False
        print(f"You have {game_attempts} attempt\nGame Over!")
    elif user_age_guess < age and user_weight_guess < weight and game_attempts == 0:
        game_is_on = False
        print(f"You have {game_attempts} attempt\nGame Over!")
    elif user_age_guess <= 2 or user_weight_guess >= 800 and game_attempts == 0:
        game_is_on = False
        print("The age and weight you entered is not within a normal age and weight\nGame Over")
        
    else:
        print("Game Over!")


'''




