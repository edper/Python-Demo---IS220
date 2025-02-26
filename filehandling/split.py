# Open the file for reading
f = open("file.dat","r")

# Read the text file one line at a time
while True:
    # Read one line from the text file
    line = f.readline()
    # Remove extra spaces and the new line
    line = line.strip()
    # Test if EOF
    if line=="":
        break
    words = line.split()
    counter = 1
    for word in words:
        print("Word Number: ",counter,": \"",word.strip(),"\"",end=" ")
        counter += 1
    print("")
# Close the buffer of a file
f.close()