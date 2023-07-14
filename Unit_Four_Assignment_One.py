#
#
#
#
#Author: Onyebuchi Iyase
#Program: Recursive Power function
#

'''
Program Guide:
    Unit Four Assignment One 
    Due Mar 26 by 11:59pm Points 6 Submitting a file upload Available Mar 14 at 12am - Mar 28 at 11:59pm
    The built in Python function pow(x,y) returns the number x to the power of y.
    Write a function that performs this task recursively.

    Name it myPow() and have it accept two integers as arguments.
    You do not have to handle a power less than 1, (myPow(64,.5) for example.  

    Test it with myPow(7,3), myPow(2,6) and one example of your choosing.

    (Hint: think about what exponentiation really is and consult the multiplication example we look at in the slides.
    This should not be hard.)
'''
# myPow function, first input the power number
# second input, the number to raise the power to.
# return the function first checks for the base case of 2 input being zero, and returns 1 as the result.
# If second is negative, the function
# inverts first number and the exponent to make 2nd input positive, and then divides 1 by the result.
def myPow(x, y):
    if y == 0:
        return 1
    elif y < 0:
        return 1 / myPow(x, -y)
    elif y % 2 == 0:
        return myPow(x*x, y//2)
    else:
        return x * myPow(x, y-1)
    
# Testing myPow() function with three tuples: (7, 3), (2, 6)
#print(f"The number 7 to the power of 3: {myPow(7, 3)}")   
#print(f"The number 2 to the power of 6: {myPow(2, 6)}")

# Testing with user into input:
num_pow = int(input("Enter the power number: "))
num = int(input("Enter the number to raise the power to: "))
print(f"The number {num_pow} to the power of {num} is: {myPow(num_pow, num)}")