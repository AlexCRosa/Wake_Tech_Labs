#
# Alex Cesar Rosa
# 5/28/2024
#

player1 = input("Enter R for rock, P for paper or S for scissors: ").lower()
player2 = input("Enter R for rock, P for paper or S for scissors: ").lower()

# Check for invalid input
if player1 not in ("r", "p", "s") or player2 not in ("r", "p", "s"):
    print("Game canceled because of invalid entry")

# Same choices = Tie
elif player1 == player2:
    print("Tie")

# Cases where player 1 wins
elif (player1 == "r" and player2 == "s") or (
        player1 == "s" and player2 == "p") or (
        player1 == "p" and player2 == "r"):
    print("Player 1 has won the game.")

# Cases where player 2 wins
elif (player1 == "r" and player2 == "p") or (
        player1 == "s" and player2 == "r") or (
        player1 == "p" and player2 == "s"):
    print("Player 2 has won the game.")
