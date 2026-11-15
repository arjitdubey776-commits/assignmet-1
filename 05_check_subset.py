first = list(map(int, input("Enter first list: ").split()))
second = list(map(int, input("Enter second list: ").split()))

is_subset = True

for item in second:
    if item not in first:
        is_subset = False
        break

if is_subset:
    print("Second list is a subset of first list")
else:
    print("Second list is not a subset of first list")
