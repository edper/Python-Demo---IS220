cipherText = input("Enter the cipher text : ")
distance = int(input("Enter the distance value : "))

decipher = ""

for letter in cipherText:
    plain = chr(ord(letter)-distance)
    if ord(plain) < ord('a'):
        letterValue =  ord('z') - (ord('a') - ord(plain) + 1)
        plain = chr(letterValue)
    decipher += plain

print(decipher)