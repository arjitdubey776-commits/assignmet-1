def find_sum(num):
    if num == 0:
        return 0
    return num + find_sum(num - 1)

num = int(input("Enter a non-negative number: "))

if num < 0:
    print("Enter a non-negative number")
else:
    print("Sum:", find_sum(num))
