import math
input1 = input("Enter the first number: ")
input2 = input("Enter the second number: ")
if input1 or input2 != type(int):
    print("You must include two numbers")
char = input("Enter the operator: ")
if char == "*":
    print(f"{input1 + input2}")
elif char == "+":
    print(f"{input1 + input2}")
elif char == "-":
    print(f"{input1 - input2}")
elif char == "/":
    print(f"{input1 / input2}")
else:
    print("This is not a valid operator.")
    
