#
# Alex Rosa
# 1/10/2024
# This program plays the classic Rock, Paper, Scissors game with the user.
# The user makes a choice and then indicates the number of times the
# computer should make a choice. The results of all games played are
# shown along with a summary of results.
#
import random

# Constants
WIN = 1
LOSE = 2
TIE = 3
ROCK = 0
PAPER = 1
SCISSORS = 2


def main():
    choices = ['rock', 'paper', 'scissors']
    print("Let's play Rock Paper Scissors!")
    print()
    user_choice = get_user_choice()
    number_plays = get_number_plays()

    print(f'User chooses {choices[user_choice]}')
    wins = 0
    ties = 0
    losses = 0
    for i in range(number_plays):
        computer_choice = random.randint(0, 2)
        print(f'Game {i + 1}: {choices[user_choice]} vs. {choices[computer_choice]} - ', end='')
        result = declare_results(user_choice, computer_choice)
        if result == WIN:
            print('Player wins!')
            wins += 1
        elif result == TIE:
            print('Tie')
            ties += 1
        else:  # LOSE
            print('Player loses.')
            losses += 1

    print(f"Results for Player: {wins} wins, {losses} losses, {ties} ties")


def get_user_choice():
    """
    This function asks whether the player chooses Rock, Paper, or Scissors
    for their play. It will be used in all the games with the computer.
    :return: user_choice
    """
    while True:
        try:
            user_choice = int(
                input('Enter 1 for Rock, 2 for Paper, or 3 for Scissors: '))
            if user_choice not in [1, 2, 3]:
                raise ()
        except:
            print('You choice should be 1, 2, or 3.')
        else:
            user_choice -= 1  # account for zero-indexing
            break
    return user_choice


def get_number_plays():
    """
    This function asks for the number of times the computer should play
    the game against the player's choice.
    :return: number_plays
    """
    while True:
        try:
            number_plays = int(
                input("How many times for computer to choose (1-50): "))
            if number_plays < 1 or number_plays > 50:
                raise ()
        except:
            print("Choose a number between 1 and 50.")
        else:
            break
    return number_plays


def declare_results(user_choice, computer_choice):
    """
    This function determines whether a player wins against the computer.
    :param user_choice:Choice made by player
    :param computer_choice:Choice made by computer
    :return:result of game
    """
    win_combos = [(ROCK, SCISSORS), (PAPER, ROCK), (SCISSORS, PAPER)]

    if (user_choice, computer_choice) in win_combos:
        return WIN
    elif (computer_choice, user_choice) in win_combos:
        return LOSE
    else:
        return TIE


main()
