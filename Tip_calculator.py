#if the bill was $150.00, split between 5 people, with 12% tip
#each person should pay (150.00 / 5) * 1.12

#checking each one, $150 is the initial bill (user_input)
#percent_tip = 12 / 100
#print(percent_tip)
#bill_with_tip = 150 * percent_tip
#print(bill_with_tip)

#total_bill = 150 + bill_with_tip
#split_the_bill = total_bill / 5
#print(split_the_bill)

print("Welcome to the tip calculator!")
#ask the user for the amount of the bill and convert it into a float or decimal
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))

#1.get the percentage of the bill, multiply by the bill
#2.Add the result to the original bill
#3.bill_with_tip = tip / 100 * bill + bill
#Another way of doing this: 
#5.bill_with_tip = bill * (1 + tip / 100)
#6print(bill_with_tip)

#Splitting each one
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people

final_amount = round(bill_per_person, 2)
#1. formatting the final amount to display two decimal place
#2. using built-in format() function

final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay ${final_amount}")
