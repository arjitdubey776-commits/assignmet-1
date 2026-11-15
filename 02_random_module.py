import random

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

if start <= end:
    print("Random number:", random.randint(start, end))
else:
    print("Starting number must be less than or equal to ending number")
