# Make a python program that would compute
# the factorial value of any integer
# Factorial notation looks like this n! 
# where n is an integer.
# For example 5! is 1 * 2 * 3 * 4 * 5 = 120
# Also give the sum of the range of values starting from 1 to that inputted integer.
# For example if 5! so the number is 5 or
# in this case add numbers 1 + 2 + 3 + 4 + 5 = 15

#INPUT
num = int(input("Enter an integer value for factorial : "))
#PROCESS
fact = 1
sum = 0
for val in range(num):
    fact = fact * (val + 1) 
    sum = sum + (val + 1)

#OUTPUT
print("The factorial value of",num,"is", fact)
print("The sum total of range from 1 to",num,"is", sum)