#INPUT
base = int(input("Enter the base of a number : "))
exponential_value = int(input("Enter the exponential value : "))

#PROCESS
product = 1
for val in range(exponential_value):
    product = product * base

#OUTPUT
print(base,"raise to the power of",exponential_value,"is",product)