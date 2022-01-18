#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#Write your code below this line 👇
print("Welcome to the tip calculator.")
tot_bill = input("What was the total bill? $")
tip_percent = input("What percentage tip would you like to give? 10, 12, or 15? ")
split_count = input("How many people to split the bill? ")
each_bill = float(tot_bill) * (1 + int(tip_percent) / 100) / int(split_count)
message = f"Each person should pay: ${each_bill:.2f}"
print(message)
