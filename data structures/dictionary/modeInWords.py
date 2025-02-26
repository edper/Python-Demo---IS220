import os
import sys

fileName = input("Enter the file name: ")

if not os.path.exists(fileName):
    print("File name does not exists!")
    sys.exit()

f = open(fileName)

words = []

# Build a list for the words
for line in f:
    for word in line.split():
        words.append(word.upper())

# Build the dictionary and give count for each words in terms of frequency
theDictionary = {}
for word in words:
    count = theDictionary.get(word,None)
    if count == None:
        theDictionary[word] = 1
    else:
        theDictionary[word] = count + 1

highestCount = max(theDictionary.values())

# Check which word has the highest count or the mode
for key in theDictionary:
    if theDictionary[key] == highestCount:
        print("The mode or the word that has the highest count is :"
              ,key,"and has the count of",highestCount)
        break