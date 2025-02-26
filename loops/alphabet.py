# Using python loop through the alphabet
# from A to Z

for letter in range(65,91):
    print(chr(letter),end=" ")

print("\n")

for alpha in range(ord('A'),ord('Z')+1):
    print(chr(alpha),end=" ")

print("\n")
for alpha in range(ord('A'),ord('Z')+1):
    print(chr(alpha)+chr(alpha+32),end=" ")