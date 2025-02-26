plainText = input("Input a one word lower-case letters: ")
distance = int(input("Input the cipher distance: "))

cipherText = ""
for ch in plainText:
    ordNum = ord(ch)
    if ordNum >= 32 and ordNum <= 126:
        pos = ord(ch)+distance
        crypt = chr(pos)
        if pos > ord('z'):
            wrapValue = pos - ord('z')
            crypt = chr(ord('a') + wrapValue - 1)
        cipherText += crypt

print("Cypertext :",cipherText)