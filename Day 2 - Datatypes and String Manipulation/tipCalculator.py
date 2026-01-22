# We're going to build a tip calculator.
#
# If the bill was $150.00, split between 5 people, with 12% tip.
#
# Each person should pay:
#
# (150.00 / 5) * 1.12 = 33.6
#
# After formatting the result to 2 decimal places = 33.60

bill = int(input("What is the amount of bill"))
people = int(input("How many people are going to split the bill"))
tip=int(input("How much percentage you want to give tip"))

tipAmt = (bill / people) * ((100+tip)/100)

print(f"Each person should pay {tipAmt} $")