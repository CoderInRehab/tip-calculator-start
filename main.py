#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print("\t\t\t\t\tWelcome to Tip Calculator\n")

bill = input("\n\nWhat was the total bill? \t\t\t\t\t$")
percent_tip = input("\nWhat percentage tip would you like to give?\n(Don't include percent sign) 10, 12, or 15? \t")
people = input("\nHow many people to split the bill?\t\t\t\t")

bill_int = float(bill)
percent_tip_int = int(percent_tip)
person_int = int(people)

total_bill = bill_int + percent_tip_int / 100 * bill_int

bill_per_person = total_bill / person_int

#final_amount = round(bill_per_person,2)
final_amount = "{:.2f}".format(bill_per_person)
res = f"\n\nEach person should pay \t\t\t\t\t\t   {final_amount}"
print(res)
