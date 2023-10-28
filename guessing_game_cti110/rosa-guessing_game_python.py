import random
random.seed()   #Prepare random number generator


# Alex Cesar Rosa
# 2023FA.CTI.110.0003
# Test cases:
# 
# guessedNumber == randomNumber = "Well done! You hit the nail on the head."
# 
# guessedNumber != randomNumber = "Not this time! Guess another number between 1 and 10?"
# 
# guessedNumber == -999 = "See you later!
randomNumber = int(random.random() * 10) + 1
print("Guess a number from 1 to 10?")
guessedNumber = int(input())
while guessedNumber != randomNumber:
    print("Not this time! Guess another number between 1 and 10?")
    guessedNumber = int(input())
    if guessedNumber == -999:
        print("See you later!")
print("Well done! You hit the nail on the head.")
