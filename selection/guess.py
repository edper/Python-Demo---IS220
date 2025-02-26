import random
import math

smaller = int(input("Enter the smaller number: "))
bigger = int(input("Enter the bigger number: "))

numberToGuess = random.randint(smaller,bigger)
maxGuess = math.ceil(math.log(bigger-smaller))
counter = 0
found = False
while True:
    guess = int(input("Enter your guess number : "))
    counter += 1
    if counter <= maxGuess:
        if guess < numberToGuess:
            print("Number to guess is bigger than that!")
        elif guess > numberToGuess:
            print("Number to guess is smaller than that!")
        else:
            print("Correct the number to guess is",numberToGuess)
            found = True
            break
    else:
        print("Maximum Guess reached!")
        break

if found:
    print("You guess in",counter,"tries")
