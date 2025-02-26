import os

path = os.getcwd()
print(path)

files = os.listdir(path)

for file in files:
    if file.endswith(".txt"):
        print("File name:", file)