# Make a python program that will accept
# two numbers. The first number as the lesser
# number and the second number as the bigger number.
# Then display numbers between those two numbers.

# Example:
# Enter the first integer (smaller) : 5
# Enter the second integer (bigger) : 10
# Output:
# 5, 6, 7, 8, 9, 10

lesserNum = int(input("Enter the first integer (lesser) : "))
biggerNum = int(input("Enter the second integer (bigger) : "))

for num in range(lesserNum,biggerNum+1):
    print(num,end=" ")