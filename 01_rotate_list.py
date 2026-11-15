numbers = list(map(int, input("Enter list elements separated by spaces: ").split()))
k = int(input("Enter number of positions to rotate right: "))

if len(numbers) > 0:
    k = k % len(numbers)
    rotated = numbers[-k:] + numbers[:-k] if k != 0 else numbers
else:
    rotated = numbers

print("Rotated list:", rotated)
