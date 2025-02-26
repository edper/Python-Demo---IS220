import os

def displayFile(fileName):
    fileList = []
    f = open(fileName)
    lineNum = 1
    for line in f:
        print("Line",lineNum,":",line.strip())
        lineNum += 1
        fileList.append(line)

    return fileList

def promptLine(fileName):
    theList = displayFile(fileName)
    noOfLines = len(theList)
    inputLine = noOfLines

    while inputLine != 0:
        inputLine = int(input("Input line number to show : "))
        if inputLine != 0 and inputLine <= noOfLines:
            print(theList[inputLine-1].strip())
        elif inputLine > noOfLines:
                print("Line number should not be greater than",noOfLines)

def main():
    while True:
        fileName = input("Enter file name of the text file: ")
        if os.path.exists(fileName):
            promptLine(fileName)        
            break
        else:
            print("File does not exists!")


if __name__ == "__main__":
    main()