def Sum(a, b):
  return a+b
def sub(a,b):
  return a-b
def mod(a, b):
  return a//b
def div(a, b):
  return a %b
def multiple(a, b):
  return a*b

print("_______Welcome to the Calculator_____") 

print("1. for Sum")
print("2. for subtraction")
print("3. for module")
print("4, for division")
print("5, for multiplication\n")

num = int(input("Select the number that you perform the function : "))
print("\n")
if num in range(6):
  num1 = int(input("Enter the first number: "))
  num2 = int(input("Enter the second number: "))
  print("\n")
  if num == 1:
    print("The sum of numbers is : ", Sum(num1, num2))
  elif num == 2:
    print("The subtraction of numbers is : ", sub(num1, num2))
  elif num == 3:
    print("The module of numbers is : ", mod(num1, num2))
  elif num == 4:
    print("The division of numbers is : ", div(num1, num2))
  elif num == 5:
    print("The multiplication of numbers is : ", multiple(num1, num2))
else:
  print("Invalid Input.. :( ")
  

