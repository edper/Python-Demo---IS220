"""
for i in range(4):
    print("Number",i+1)

for j in range(4):
    print(j+1,end=" ")
print("\n")
for k in range(1,11):
    print("Number", k)

"""

"""
Make a python program that will display
your name five times using for loop.
"""

"""
Make a python program that will display
your state's greetings based on the number input
of how many times it should be displayed.

Example:
How many times you want me to display Kasehlelie: 3
Kasehlelie
Kasehlelie
Kasehlelie

times = int(input("How many times should I greet you Kasehelie :"))

for l in range(times):
    print("Kasehlelie")

"""


"""
Using for loop in python display numbers
1 to 5 but double its value, that is,
2, 4, 6, 8 and 10.

for x in range(5):
    print((x+1)*2)

for y in range(1,6):
    print(y*2)

"""

"""
Using for loop in python display the square
of the numbers 1 to 5 which are 1, 4, 9, 16, 25
for x in range(5):
    print((x+1)**2)

for y in range(1,6):
    print(y**2)
for x in range(0,26,5):
    print(x)

"""



"""
Using for loop in python
displays numbers from 10
to 100 with step/increment of 10
for x in range(10,101,10):
    print(x)

"""

"""
Using python for loop display numbers
from 10 to 1.
for x in range(10,0,-1):
    print(x)
"""
"""
Using python for loop display numbers
from 50 to 5 with decrement of 5.
"""
"""

print("ID","\tName","\tBalance")

id = 101
name = "John Doe"
balance = 1850.849657
#print("%-5d" % id,"%-12s" % name,"$%5.2f" % balance)
print("%-5d%-12s$%5.2f" % (id,name,balance))


id = 102
name = "Mary Jones"
balance = 2548.7598
#print("%-5d" % id,"%-12s" % name,"$%5.2f" % balance)
print("%-5d%-12s$%5.2f" % (id,name,balance))


print("\n\n")

for exponent in range(7,11):
    print("%-3d%12d" % (exponent,10**exponent))
"""

str = input("Enter your favorite quote : ")

counter=0
for ch in str:
    if ch==" ":
        counter+=1

print("The number of spaces on your favorite quote is",counter)