plainText = input("Input a one word lower-case letters: ")
distance = int(input("Input the cipher distance: "))

cipherText = ""
for ch in plainText:
    pos = (abs((32 - ord(ch)) - 1)  % 96 + distance - 1)
    crypt = chr(pos)
    cipherText += crypt

print("Cypertext :",cipherText)