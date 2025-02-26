# Accept the file name to be use as input
fileName = input("Enter the file name of the text file: ")
# open the file
f = open(fileName,"r")

# prepare an empty list for all numbers from the text file
numbers = []

# loop through the file line by line
for line in f:
    # split the line into several numbers
    num = line.split()
    # loop through the line, number by number
    for n in num:
        # add it to our list after converting it to a float
        numbers.append(float(n))

numbers.sort()
midpoint = len(numbers) // 2

# test if number of entries from the text file are odd
if len(numbers) % 2 == 1:
    # if odd get the middle number
    median = numbers[midpoint]
else:
    # if even get the middle number plus the number before that
    # and divide it by 2
    median = (numbers[midpoint] + numbers[midpoint-1]) / 2

f.close()
print("The median is",median)