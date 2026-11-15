values = tuple(map(int, input("Enter numbers separated by spaces: ").split()))

print("Tuple:", values)
print("Length:", len(values))

if len(values) > 0:
    print("Maximum:", max(values))
    print("Minimum:", min(values))
    search = int(input("Enter a number to count: "))
    print("Count:", values.count(search))
else:
    print("Tuple is empty")
