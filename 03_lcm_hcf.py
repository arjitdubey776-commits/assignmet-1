a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

x = abs(a)
y = abs(b)

while y != 0:
    x, y = y, x % y

hcf = x

if hcf == 0:
    lcm = 0
else:
    lcm = abs(a * b) // hcf

print("HCF:", hcf)
print("LCM:", lcm)
