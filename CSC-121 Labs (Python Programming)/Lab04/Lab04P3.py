##
# Alex Cesar Rosa
# 1/31/2024
# Dice game
#

import random


def main():
    rolls = int(input("How many times do you want to roll the die? "))
    while not 5 < rolls < 15:
        print("Enter a number between 5 and 15.")
        rolls = int(input("How many times do you want to roll the die? "))

    roll_die(rolls)


def roll_die(rolls):
    for roll in range(1, rolls):
        random_number = random.randint(1, 20)
        if random_number == 20:
            symbol = "CRITICAL HIT!"
        elif random_number % 4 == 0:
            symbol = "Sword"
        elif random_number % 4 == 1:
            symbol = "Shield"
        elif random_number % 4 == 2:
            symbol = "Spell"
        elif random_number % 4 == 3:
            symbol = "Potion"

        print(f"Roll {roll}: {random_number} ==> {symbol}")

    print("Thanks for playing!")


main()