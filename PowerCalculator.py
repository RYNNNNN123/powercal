base = float(input("Enter the base number: "))
exponent = int(input("Enter the power: "))

result = 1

for i in range(exponent):
    result = result * base

print("The result is:", result)