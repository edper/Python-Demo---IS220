import random

# Open the file for writing
f = open("myintegers.txt","w")

# generate 20 random numbers
for i in range(20):
    num = random.randint(1,500)
    # Write the random number to the file plus newline
    f.write(str(num) + "\n")

# close the buffer of the file
f.close()