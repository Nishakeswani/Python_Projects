#This will check the eligibility and ticket price for roller coaster ride.
height = int(input("Enter your height: \n"))
ticket = 0
if height > 120:
  print("yes you are eligible for roller coster ride")
  Age = int(input("what is your age?\n"))
  if Age < 12 :
    ticket = 5
    print("Your ticket price is 5$")  
    
  elif Age <= 18:
    ticket = 7
    print("Your ticket price is 7$")
    
  else:
    ticket = 12
    print("Your ticket price is 12$")
    

  want_photos = input("Do you want pictures: Y or N")
  if want_photos.upper() == "Y":
    #print("You need to pay 3$ exta")
    ticket += 3
    #print(f"you need to pay total {ticket}$ amount")
  print(f"your total bill is {ticket}")

else:
  print("sorry! you are noy eligible to take roller coster ride")
