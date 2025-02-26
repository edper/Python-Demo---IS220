cipherText = input("Input a one word lower-case letters: ")
distance = int(input("Input the cipher distance: "))

plainText = ""
for ch in cipherText:
    pos = ord(ch) - distance
    decrypt = chr(pos)
    if pos < ord('a'):
        wrapValue = ord('a') - pos
        decrypt = chr(ord('z') - wrapValue + 1)
    plainText += decrypt

print("Plaintext :",plainText)