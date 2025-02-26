decimal = int(input("Input an integer and I will convert to binary: "))

bitStr = ""
origDec = decimal
while True:
    remainder = decimal % 2
    decimal = decimal // 2
    bitStr = str(remainder) + bitStr
    if decimal==0:
        break

print("Binary for decimal",origDec,"is",bitStr)