decimal = int(input("Input an integer and I will convert to octal: "))

octStr = ""
origDec = decimal
while True:
    remainder = decimal % 8
    decimal = decimal // 8
    octStr = str(remainder) + octStr
    if decimal==0:
        break

print("Octal for decimal",origDec,"is",octStr)