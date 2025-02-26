# Read a file which has the scores of three quizzes for each student.
# Then compute the total score and the average score for each student.
# And then write to a file.

# File for reading the scores
fr = open("scores.txt","r")
# File for writing the total and average scores
fw = open("summary.txt","w")

while True:
    # read one student at a time
    line = fr.readline()

    # check if EOF (End-Of-File)
    if line=="":
        break

    # Split the data separated by spaces into namea and the three scores
    data = line.split()
    # The first one is the name
    name = data[0]
    # Get the total score but convert the scores into integers
    totalScore = int(data[1]) + int(data[2]) + int(data[3])
    # Get the average but round it to two decimal places
    average = round(totalScore / 3,2)
    # Write to the file
    fw.write("Name : " + name + ", Total : " + str(totalScore) + ", Average : " +str(average) + "\n")

# Close the files
fr.close()
fw.close()