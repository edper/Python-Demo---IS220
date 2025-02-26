fileList = ["myfile.txt","myprogram.exe","yourfile.txt"]

# This program will print files
# that ends with .txt
for fileName in fileList:
    if ".txt" in fileName:
        print(fileName)
fileList = ["myfile.txt.exe","myprogram.exe","yourfile.txt"]
for fileName in fileList:
    # Redo this part and check only 
    # for the last four characters
    fileExtension = fileName[-4:]
    if fileExtension == ".txt":
        print(fileName)