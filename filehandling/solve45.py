# Problem Number 1
# Write a code segment that opens a 
# file named myfile.txt for input 
# and prints the number of lines in the file.

# f = open("myfile.txt","r")
# a = open("myfile.txt","a")

# numberOfLines = 0
# for line in f:
#     numberOfLines+=1

# f.close()
# a.write("\nNumber of Lines: " + str(numberOfLines))
# a.close()

# Problem Number 2
# Write a code segment that opens a file for input 
# and prints the number of four-letter words in the file.

# f = open("somewords.txt","r")
# a = open("somewords.txt","a")

# fourWords = 0
# for line in f:
#     words = line.split()
#     for word in words:
#         word = word.strip()
#         if len(word)==4:
#             fourWords+=1
# f.close()
# a.write("\n\nNumber of four-letter words: " + str(fourWords))
# a.close()

# Problem Number 3
# Assume that a file contains integers separated by newlines. 
# Write a code segment that opens the file 
# and prints the average value of the integers.

# f = open("studscores.txt","r+")

# totalScore = 0
# numberOfScores = 0
# while True:
#     line = f.readline()
#     if line=="":
#         break
#     score = int(line.strip())
#     totalScore += score
#     numberOfScores += 1

# average = totalScore / numberOfScores
# f.write("\n\nAverage Score is : " + str(round(average,2)))
# f.close()

# Problem Number 4
# Write a code segment that prints the names 
# of all of the items in the current working directory.
# import os

# currDir = os.getcwd()
# files = os.listdir(currDir)

# for file in files:
#     print(file)

# Problem Number 5
# Write a code segment that prompts the user for a filename. 
# If the file exists, the program should print its contents 
# on the terminal. Otherwise, it should print an error message.

# import os

# file = input("Input a file name: ")

# if os.path.exists(file):
#     f = open(file)
#     lines = f.read()
#     print(lines)
#     f.close()
# else:
#     print("Error: File does not exists!")
