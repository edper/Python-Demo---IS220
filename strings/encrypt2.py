plainText = input("Input a one word lower-case letters: ")
distance = int(input("Input the cipher distance: "))

cipherText = ""
for ch in plainText:
    pos = (abs((ord('a') - ord(ch)) - 1)  % 26 + distance - 1) + ord('a')
    crypt = chr(pos)
    cipherText += crypt

print("Cypertext :",cipherText)