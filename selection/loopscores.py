
totalScore = 0
counter = 0
Done = False
while not Done:
    score = int(input("Enter score between 0 to 100 or -1 to quit : "))
    if score>=0 and score<=100:
        totalScore += score
        counter+=1
    else:
        if score != -1:
            print("Enter score between 0 to 100 only")
        else:
            Done = True

average = totalScore / counter
print("Total Score : %0.2f" % totalScore)
print("Average Score : %0.2f" % average)
#print(f"Total Score : {totalScore: .2f}")
#print(f"Average Score : {average: .2f}")

