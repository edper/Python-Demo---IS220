import os

path = "temppath"

if os.path.exists(path):
    print("The path is good!")
else:
    print("Path does not exists!")


file = "temppath\\emo.txt"

if os.path.exists(file):
    print("File exists!")
else:
    print("Files does not exists!")