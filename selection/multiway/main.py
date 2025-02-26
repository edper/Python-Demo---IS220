"""
    Make a program that will give the letter grade of a given score.
    For scores 90 and above the letter grade is A
    For scores 80 and below 90 the letter grade is B
    For scores 70 and below 80 the letter grade is C
    For scores 60 and below 70 the letter grade is D
    For scores below 60 the letter grade is F
"""

# score = int(input("Enter the score and I'll give you the grade : "))

# if score>=90:
#     letterGrade = "A"
# elif score>=80:
#     letterGrade = "B"
# elif score>=70:
#     letterGrade = "C"
# elif score>=60:
#     letterGrade = "D"
# else:
#     letterGrade = "F"

# print("Your score is",score,"and your grade is",letterGrade)

# ratingScore = int(input("Input Rating Score of a hotel : "))

# if ratingScore>=9:
#     remarks = "Excellent"
# elif ratingScore==8:
#     remarks = "Very Good"
# elif ratingScore>=5:
#     remarks = "Good"
# else:
#     remarks = "Poor"

# print("Remarks for your score : ",remarks)

# num = 10

# if num < 0 or num > 100:
#     print("Number should be between 0 and 100. But your number is",num)
# else:
#     print("Your number is between 0 and 100 which is", num)






# Input:
status= input("Is the parent single?: ")
monthlysalary=float(input("Enter the monthly salary for the parent:$ "))

#Process:
taxrate= 0.085
if status=="Yes":
    taxrate= (monthlysalary-500) * 0.085

Net_salary= monthlysalary- taxrate

#Output: Tax and Next Salary
print("The Tax is $%0.2f"%taxrate)
print("The Net Salary is $%0.2f"%Net_salary)
