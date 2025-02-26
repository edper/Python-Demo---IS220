decimal = int(input("Input an integer and I will convert to hexa: "))

hexaStr = ""
origDec = decimal
while True:
    remainder = decimal % 16
    decimal = decimal // 16
    if remainder < 10:
        hexaStr = str(remainder) + hexaStr
    else:
        hexaStr = chr(55+remainder) + hexaStr
    if decimal==0:
        break

print("Hexadecimal for decimal",origDec,"is",hexaStr)