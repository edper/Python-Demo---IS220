# Open the file for reading
f = open("file.dat","r")

# Read the text file
lines = f.read()

# Print the content of the text file
print(lines)

# Close the buffer of a file
f.close()