binaryNum = input("Enter a binary string: ")


decimal = 0
exponent = len(binaryNum) - 1
for bit in binaryNum:
    num = int(bit) * 2**exponent
    decimal += num
    exponent -= 1

print("Decimal value for",binaryNum,"is",decimal)
