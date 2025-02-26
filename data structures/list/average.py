def average(numList):
    sum = 0
    for num in numList:
        sum += num
    avg = sum / len(numList)
    return avg

avgValue = average([10,5,8])
print("The average is", round(avgValue,2))