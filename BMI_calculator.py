#This is a BMI calculator
height = float(input("enter your height\n"))
weight = float(input("enter your weight\n"))

bmi = round(weight / (height**2))

if bmi < 18.5:
  print(f"you are underweight with bmi {bmi}")
elif bmi < 25:
  print(f"you are normal weight with bmi {bmi}")
elif bmi < 30:
  print(f"you are overweight with bmi {bmi}")
elif bmi < 35:
  print(f"you are obese with bmi {bmi}")
else:
  print(f"you are clinically obese with bmi {bmi}")
