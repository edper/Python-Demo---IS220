octalNum = input("Enter a octal string: ")

decimal = 0
exponent = len(octalNum) - 1
for digit in octalNum:
    num = int(digit) * 8**exponent
    decimal += num
    exponent -= 1

print("Decimal value for",octalNum,"is",decimal)
