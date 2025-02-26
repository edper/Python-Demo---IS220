# One-way selection

"""
 Make a Python program that gets the absolute value of an integer.
"""


# value = int(input("Give me an integer and I will give you its absolute value: "))

# abs = value

# # One-way selection
# if value < 0:
#     abs = value * -1

# print("The absolute value of",value,"is",abs)

"""
Make a python program using one-way selection
that would give a discount for purchases of at least $100.
The discount from ABC store is 10%. Otherwise no discount.
Display the Total Payable amount whether discounted or not.
"""

# INPUT: purchase amount
# OUTPUT : discounted price
# PROCESS : Test purchase amount if at least $100 then give a discount of 10%


# purchaseAmount = float(input("Enter the purchase amount: "))

# discountedPrice = purchaseAmount

# if purchaseAmount>=100:
#     discountedPrice = purchaseAmount - purchaseAmount * 0.10

# print("Total Payable Amount $%0.2f " % discountedPrice)

"""
The KAMORALE college offers an outright $200 credit
if you enroll this semester. However, if your GPA
the last semester is 3.0 and above they will give
you a 25% discount of your Total Tuition Fee.
Make a Python program that will accept the Total Tuition Fee
and using one-way selection determine if the student will
have a 25% Tutition Fee discount. Your program then
will output the Net Tuition Fee that the student needs to pay.
"""



# start_amount = float(input("Enter the first amount amount: "))

# starting_year = int(input("Enter the number of starting year: "))

# ending_year = int(input("Enter amount of ending year: "))

# rate = int(input("Enter the rate as %: "))



# Per_Credit_Amount = start_amount

# total_interest = 0



# print("%-6s%-18s%10s%15s" % ("Year", "Per Credit Amount","Interest","Running Total"))




# for year in range(starting_year-1,ending_year,5):

#     interest = Per_Credit_Amount * (rate / 100)

#     running_total = Per_Credit_Amount + interest

#     total_interest += interest

#     print("%4d%18.2f%10.2f%15.2f" %

#            (year+1,Per_Credit_Amount, interest, running_total))

#     Per_Credit_Amount += interest



# print("Ending Running Total:","$%8.2f" % running_total)

# print("Total Interest:","$%8.2f" % total_interest)

# # INPUT - GPA and Total Tuition Fee
# totalTuitionFee = float(input("Enter the Total Tuition Fee of the student : "))
# GPA = float(input("Enter the student's GPA : "))

# # PROCESS
# outRightCredit = 200
# discount = 0

# if GPA>=3.0:
#     discount = totalTuitionFee * 0.25

# netTuitionFee = totalTuitionFee - outRightCredit - discount

# # OUTPUT Net Tuition Fee
# print("The Net Tuition Fee is $%0.2f" % netTuitionFee)


# gender = input("Enter Gender (Male/Female) : ")

# if gender.lower() == "male":
#     print("Gender is Male")
# else:
#     print("Gender is Female")

"""
Make a python program that will accept two integers
and determine which is the bigger value and the smaller
value between the two.
For example if the is 10 and 5, the bigger value is 10
and the smaller value is 5.
"""

# firstVal = int(input("Enter the first number : "))
# secondVal = int(input("Enter the second number : "))

# if firstVal > secondVal:
#     print("The bigger number is",firstVal)
#     print("The smaller number is",secondVal)
# else:
#     print("The bigger number is",secondVal)
#     print("The smaller number is",firstVal)

# Make python program using two-way selection
# that would determine if the student pass or not 
# using the score.
# If the student score is 70 and above display pass
# otherwise display fail.

# count = int(input("Number of quizzes : "))
# sum = int(input("Total Scores : "))

# if count>0 and sum:
#     average = sum / count
#     print("The average is %0.2f" % average)
# else:
#     print("Count should be more than zero")


# num = int(input("Enter an integer and I'll give its absolute value : "))

# abs = num
# if num<0:
#    abs = num * -1

# # print(f"The absolute value of {num} is {abs}")
# print("The absolute value of",num,"is",abs)


# str1 = input("Input a string : ")
# str2 = input("Input another string : ")

# if str1>str2:
#    print(str2)
#    print(str1)
# else:
#    print(str1)
#    print(str2)


# valid = True

# acc = ""
# while True:
#    str = input("")
#    if str in range(0,10):
#       acc += str
#    else:
#       valid = False
#       break 

# if valid:
#    num = int(acc)
#    print("The number is",num)
# else:
#    print("That is not a valid number")


# state = input("Enter the state initial : ").upper()

# if state=="P":
#     print("Pohnpei")
# elif state == "C":
#     print("Chuuk")
# elif state == "Y":
#     print("Yap")
# elif state == "K":
#     print("Kosrae")
# else:
#     print("It should be either P, C, Y or K")

# firstNum = int(input("Enter the first number : "))
# secondNum = int(input("Enter the second number : "))
# op = input("Enter the arithmetic operator (+, -, *, /) : ")

# valid = True
# if op=="+":
#     res = firstNum + secondNum
# elif op=="-":
#     res = firstNum - secondNum
# elif op=="*":
#     res = firstNum * secondNum
# elif op=="/":
#     if secondNum==0:
#         print("Divisible by zero is not allowed")
#         valid = False
#     else:
#       res = firstNum / secondNum
# else:
#     print("Operator is invalid")
#     valid = False

# if valid:
#     print(firstNum,op,secondNum,"=",res)


# Sentinel-controlled loop
# total = 0
# counter = 0
# num = input("Enter a number and press Enter to quit: ")
# while num != "":
#     value = float(num)
#     total += value
#     counter += 1
#     num = input("Enter a number and press Enter to quit: ")

# average = total / counter
# print("Total Score : %0.2f" % total)
# print("Average Score : %0.2f" % average)


# total = 0
# counter = 0
# num = float(input("Enter a number and press Enter to quit: "))
# while int(num) != -1:
#     value = float(num)
#     total += value
#     counter += 1
#     num = float(input("Enter a number and press Enter to quit: "))

# average = total / counter
# print("Total Score : %0.2f" % total)
# print("Average Score : %0.2f" % average)


# num = 10
# found = False

# while not found:
#     guess = int(input("Guess the number that I have : "))
#     if guess < num:
#         print("The number is bigger than that.")
#     elif guess > num:
#         print("The number is smaller than that.")
#     else:
#         print("Congratulations! You guess the number right.")
#         break


x = 1
print("\t 1\t 2\t 3\t 4\t 5\t 6\t 7\t 8\t 9\t 10")
print("-"*83)
while x <= 10:
     y = 1
     str_length = len(str(x))
     print(x,(3-str_length)*" ","|",end="")
          
     while y<=10:
          print("\t",x*y,end="")
          y+=1
     print("")
     x+=1

print("\n\n")
print("\t 1\t 2\t 3\t 4\t 5\t 6\t 7\t 8\t 9\t 10")
print("-"*83)
for a in range(1,11):
     print(a,end="")
     for b in range(1,11):
          print("\t",a*b,end="")
     print("")


# Guessing Game (Random Number)
# Guess the number that I have

import random

num = int(random.random() * 100)

found = False

while not found:
    guess = int(input("Guess the number that I have : "))
    if guess < num:
        print("The number is bigger than that.")
    elif guess > num:
        print("The number is smaller than that.")
    else:
        print("Congratulations! You guess the number right.")
        break

