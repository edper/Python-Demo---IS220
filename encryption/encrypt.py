plainText = input("Enter a word in lowercase alphabet : ")
distance = int(input("Enter the distance value : "))

cipher = ""

for letter in plainText:
    letterValue = ord(letter)+distance
    if letterValue > ord('z'):
        letterValue = ord('a') + (letterValue - ord('z')) - 1
    crypt = chr(letterValue)
    cipher += crypt

print(cipher)

