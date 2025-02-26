# firstNum = int(input("Enter the first integer number : "))
# secondNum = int(input("Enter the second integer number : "))

# if firstNum>secondNum:
#     maxNum = firstNum
#     minNum = secondNum
# else:
#     maxNum = secondNum
#     minNum = firstNum

# print("The bigger number is",maxNum,"and the smaller number is",minNum)

#INPUT
purchaseAmount = float(input("Enter the purchase amount : "))

#PROCESS
if purchaseAmount>=199:
    discount = purchaseAmount * 0.08
else:
    discount = purchaseAmount * 0.05

discountedPrice = purchaseAmount - discount

#OUTPUT
print("Purchase Amount - $%0.2f" % purchaseAmount)
print("Discount - $%0.2f" % discount)
print("Discounted Price - $%0.2f" % discountedPrice)
