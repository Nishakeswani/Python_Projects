#This will check the eligibility and ticket price for roller coaster ride.
height = int(input("Enter your height: \n"))

if height > 120:
  print("yes you are eligible for roller coster ride")
  Age = int(input("what is your age?\n"))
  if Age < 12 :
    print("Your ticket price is 5$")  
    ticket = 5
  elif Age <= 18:
    print("Your ticket price is 7$")
    ticket = 7
  else:
    print("Your ticket price is 12$")
    ticket = 12

  want_photos = input("Do you want pictures: Y or N")
  if want_photos.upper() == "Y":
    print("You need to pay 3$ exta")
    Total_ticket = ticket + 3
    print(f"you need to pay total {Total_ticket}$ amount")
  else:
    print(f"you need to pay total {ticket}$ amount")
    
else:
  print("sorry! you are noy eligible to take roller coster ride")
  
