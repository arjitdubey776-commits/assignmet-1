num = int(input("Enter a number: "))

square = num * num
digits = len(str(abs(num)))

if square % (10 ** digits) == num:
    print("Automorphic number")
else:
    print("Not an automorphic number")
