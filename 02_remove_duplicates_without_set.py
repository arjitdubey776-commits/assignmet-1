numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
result = []

for num in numbers:
    if num not in result:
        result.append(num)

print("List without duplicates:", result)
