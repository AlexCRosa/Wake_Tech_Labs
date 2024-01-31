##
# Alex Cesar Rosa
# 1/31/2024
# Trish's Swap Shop Calculator
#
# Global Constants

BOOK_PRICE = 2.25
DVD_PRICE = 4.35
GAME_PRICE = 5.00
TAX_RATE = 0.065  # Tax Rate of 6.5%


def main():  # DO NOT CHANGE ANY CODE IN THE MAIN ROUTINE
    # NOTE: This program is NOT doing input validation to simplify the
    # program. To do input validation we would need to insert these lines
    # into while loops.
    num_books = int(input('Enter the number of books: '))
    num_dvds = int(input('Enter the number of DVDs: '))
    num_games = int(input('Enter the number of games: '))

    calc_and_display_total(num_books, num_dvds, num_games)


# Create a function called calc_and_display_total. It should take
# 3 parameters. Use the names provided here:
#    books  - Number of books
#    dvds  - Number of dvds
#    games  - Number of games
#
# It should calculate and display the total cost of each item. It should also
# calculate and display the total cost with tax.


def calc_and_display_total(books, dvds, games):
    #  Receive and process input
    total_books = books * BOOK_PRICE
    total_dvds = dvds * DVD_PRICE
    total_games = games * GAME_PRICE

    subtotal = total_books + total_dvds + total_games
    tax = subtotal * TAX_RATE
    total = subtotal + tax

    # Output
    print(f"Books: ${total_books:.2f}")
    print(f"DVDs: ${total_dvds:.2f}")
    print(f"Games: ${total_games:.2f}")

    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total: ${total:.2f}")


main()
