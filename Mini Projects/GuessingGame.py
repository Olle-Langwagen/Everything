import random

#Guess the number
print("Guess a number between 0 and 10")
theNumber = random.randrange(0, 10)
number = -1
while theNumber != number:
    number = int(input("Guess the number: "))
print("Congratulations! You guessed the right number")