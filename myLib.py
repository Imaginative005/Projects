# Creating the constant variable Hodges:
Hodges = 14


def isHarshad(num):
    # Calculating the sum of digits of the number
    digit_sum = sum([int(digit) for digit in str(num)])
    # Checking if the number is divisible by the sum of its digits
    if num % digit_sum == 0:
        return True
    else:
        return False


# Creating the function isSiete():
def isSiete(num):
    # Extracting the second digit from the number
    tens_place = str(num)[1]
    # Checking if the second digit is equal to '7'
    if tens_place == '7':
        return True
    else:
        return False
