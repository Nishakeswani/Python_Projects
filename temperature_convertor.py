#This is a simple temperature convertor in python language

temp = float(input("Enter the Temperature"))
convert = input("So, You want temp in fahrenheit type F or in Celsius then type C")

if convert.upper() == "F":
  temp_f = temp*(9/5) + 32
  print("remperature in fahrenheit is : ", temp_f)
elif convert.upper() == "C":
  temp_c = temp - 32 * (5/9)
  print("temperature in Celsus is : ", temp_c)
else: 
  print("invalid input")  
