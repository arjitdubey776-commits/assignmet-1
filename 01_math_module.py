import math

num = float(input("Enter a number: "))

print("Square root:", math.sqrt(num))
print("Factorial requires a non-negative integer")
if num >= 0 and num.is_integer():
    print("Factorial:", math.factorial(int(num)))
