#
# Alex Cesar Rosa
# 1/17/2024
# Card Game Action
#

# All FillThisIn should be replaced with correct code
FillThisIn = None

# This will be filled in with what we output
# to the user.
action = ''

# Get the card information from the user.
color = input('Enter the color of the card: ')
number = int(input('Enter the number on the card: '))

# Determine if the card information is valid.
if color != 'Red' and color != 'Black':  # Check if color is correct
    action = 'Card color is not valid'
elif number < 2 or number > 10:  # Check if number is out of range
    action = 'Card number out of range'

# Card data is valid.
# Determine the action for the card.
else:
    # Card is Red and number is even
    if color == 'Red' and number % 2 == 0:
        action = 'Discard 2 cards'

    # Card is Red and number is odd
    elif color == 'Red' and number % 2 != 0:
        action = 'Draw 1 card'

    # Card is Black and number is even
    elif color == 'Black' and number % 2 == 0:
        action = 'Play another card'

    # All other conditions false, card is Black and odd
    else:
        action = "Skip next player's turn"

print(f'Action: {action}')
