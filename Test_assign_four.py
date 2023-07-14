#myPow() function in Python:


def myPow(x, y):
    if y == 0:
        return 1
    elif y < 0:
        return 1 / myPow(x, -y)
    elif y % 2 == 0:
        return myPow(x*x, y//2)
    else:
        return x * myPow(x, y-1)
'''
The function first checks for the base case of y being zero, and returns 1 as the result. If y is negative, the function inverts x and the exponent to make y positive, and then divides 1 by the result.

If y is even, it recursively calls myPow() with x*x and y//2 as arguments.
This takes advantage of the property that x^y = (x^2)^(y/2) for even y.

If y is odd, the function recursively calls myPow() with x and y-1 as arguments,
and then multiplies the result by x. This is based on the property that x^y = x * x^(y-1) for odd y.

To test the function, we can call it with the given examples:

'''
print(myPow(7, 3))   # Output: 343
print(myPow(2, 6))   # Output: 64
print(myPow(5, 4))   # Output: 625
#This should return the expected values of 343, 64, and 625, respectively.