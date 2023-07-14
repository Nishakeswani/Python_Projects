#This will calculate the % of love between two people
name1 = input("enter your name:\n")
name2 = input("enter your partner's name: \n")

name1 = name1.lower()
name2 = name2.lower()

combined = name1 + name2

t = combined.count("t")
r = combined.count("r")
u = combined.count("u")
e = combined.count("e")

l = combined.count("l")
o = combined.count("o")
v = combined.count("v")

first = t+r+u+e
second = l+o+v+e

print(first)
print(second)

love = str(first) + str(second)

love = int(love)

#print(f"Your love percentage is {love}%")

if (love < 10) or (love > 90):
  print(f"your score is {love}% , you go together like coke and mentos")
elif (love > 40) or (love < 50):
  print(f" your score is {love}% , you are alright together")
else:
  print(f"your score is {love}%")


