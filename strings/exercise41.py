data = "myprogram.exe"
# 1
print(data[2]) # 'p'
print(data[-1]) # last letter 'e'
print(len(data)) # 13
print(data[0:8]) # 'myprogra'
# 2
print(data[5:9]) # 'gram'
print(data[0:9]) # 'myprogram'
print(data[len(data) // 2]) # 'r'
# 3
print("\n")
myString = "John Doe"
print(myString)
for i in range(len(myString)-1,-1,-1):
    print(myString[i],end="")

# 4
print("\n")
reversedString = ""
for i in range(len(myString)-1,-1,-1):
    reversedString += myString[i]

print("Original String:",myString)
print("Reversed String:",reversedString)

