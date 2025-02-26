
num = 5

print("Number",num,"pts") # without formatting
print("Number %-2d" % num,"pts") # with decimal formatting 2 character but space when empty to the right
print("Number %2d" % num,"pts") # with decimal formatting 2 character but space when empty to the left
print("Number %-4d" % num,"pts") # with decimal formatting 4 character but space when empty to the right
print("Number %4d" % num,"pts") # with decimal formatting 4 character but space when empty to the left
print("Number %0.2f" % num,"pts") # with float formatting in 2 decimal places

studentName = "John Doe"
print("Name: %20s" % studentName) # with string formatting spaces to the left including the string
print("Name: %-20s" % studentName," - Passed") # with string formatting spaces to the right including the string