#num = int(input("Enter a number: "))
def isHarshad(num):
    digit_sum = sum(map(int, str(num)))
    return num % digit_sum == 0
harshad_numbers = []
for num in range(1, 501):
    if isHarshad(num):
        harshad_numbers.append(num)

# using list comprehension
harshad_numbers = [num for num in range(1, 501) if isHarshad(num)]
print(harshad_numbers)
