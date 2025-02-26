hexaNum = input("Enter a hexadecimal string: ")

decimal = 0
exponent = len(hexaNum) - 1
for digit in hexaNum:
    if digit in "AaBbCcDdEeFf":
       letter = digit.upper()
       digit = ord(letter) - 55
       num = digit * 16**exponent
    elif digit in "0123456789":
       num = int(digit) * 16**exponent
    else:
       num = 0
              
    decimal += num
    exponent -= 1

print("Decimal value for hexadecimal",hexaNum,"is",decimal)
