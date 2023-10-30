import random
random.seed()   #Prepare random number generator

# Alex Cesar Rosa

# Test cases:
# guessedNumber == randomNumber = "Well done! You hit the nail on the head."
# guessedNumber != randomNumber = "Not this time! Guess another number between 1 and 10?"
# guessedNumber == -999 = "See you later!

randomNumber = int(random.random() * 10) + 1

guessedNumber = int(input("Guess a number from 1 to 10? "))

while guessedNumber != randomNumber:
    guessedNumber = int(input("Not this time! Guess another number between 1 and 10? "))
    if guessedNumber == -999:
        print("See you later!")
        break
    if guessedNumber == randomNumber:
        print("Well done! You hit the nail on the head.")
