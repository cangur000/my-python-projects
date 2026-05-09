num1 = int(0)
num2 = int(1)
sum = int(num1 + num2)
while sum < 10000:
    print(f"{sum}")
    sum = sum + num2
    num2 = sum - num2

