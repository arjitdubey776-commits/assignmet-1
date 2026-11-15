numbers = list(map(int, input("Enter numbers from 1 to n with one missing: ").split()))
n = int(input("Enter n: "))

expected_sum = n * (n + 1) // 2
actual_sum = sum(numbers)

print("Missing number:", expected_sum - actual_sum)
