#you come to pizza cafe and ordered 1 pizza with some specificateion. based on that It will give you a final price.

print("Welcome to Pizza coner")
bill = 0 
size = input("enter the size you want to buy S , M, L")
if size.upper() == "S":
  bill += 15
  print("Small pizza is of 15$")
elif size.upper() == "M":
  bill += 20
  print("Medium pizza is of 20$")
else: 
  bill += 25
  print("large pizza is of 25$")

Add_pepperoni = input("Do you want to add perperoni?? Y or N")

if Add_pepperoni.upper() == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3


Add_cheese = input("Do you want extra cheese? Y or N")
if Add_cheese.upper() == "Y":
  bill += 1

print (f"your total bill is {bill}$")
