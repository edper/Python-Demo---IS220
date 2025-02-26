# function that has no parameter
# does not return a value
def sayHello():
    print("Hello")

# function that has a parameter
# and returns a value
def square(num):
    return num * num

def cube(num):
    return num * num * num

# this one has more detailed body of a function
def sumTotal(myList):
    sum = 0
    for num in myList:
        sum += num

    return sum

# function that has two parameters
def percent(amount,per):
    percentage = amount * per/100
    return percentage

def main():
    # invoke or call the function
    sayHello()
    # you could also call a function inside a function like print
    print("Square of 5 is",square(5))
    print("Cube of 5 is",cube(5))
    print("The sum of the list is",sumTotal([1,2,3,4,5]))

    price = 100
    discount = 10
    # invoke a function inside a formula
    discounted = price - percent(price,discount)
    print("The price is",price)
    print("The discount percentage is",str(discount)+"%")
    print("The discounted Amount %0.2f" % discounted)

# Test if there is a main function and invoke it
if __name__ == "__main__":
    main()
