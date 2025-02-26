# Make a python program
# that will accept a string
# and display with space in between

# Example
# Enter a string : John
# J o h n

myString = input("Enter a string : ")

for letter in myString:
    print(letter,end=" ")

# Use another loop here to reverse the string
# nhoJ
# Tip: use len() function or yourString.__len__()
# Use also range but in reverse
# For a string it starts with zero until length of the string - 1
# "Hello" str[0] = "H", str[4]="o", str[5] error: out of bounds index

revStr=""
for char in range(len(myString)-1,-1,-1):
    revStr = revStr + myString[char]

print("\nThe reverse of",myString,"is",revStr)