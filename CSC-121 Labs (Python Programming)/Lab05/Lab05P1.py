#
# Alex Cesar Rosa
# 2/5/2024
# This program calculates the total cost for items purchased at Bargain
# Used Books. The program outputs the total cost before tax, the sales tax,
# and the total after tax.
#
# DO NOT MAKE ANY OTHER CHANGES TO THE CODE THIS FILE!
from itemProcessor import get_item_count, get_item_total, calc_and_display_receipt

BOOK_PRICE = 2.25
DVD_PRICE = 4.35
GAME_PRICE = 5.00
BOOK_MAX = 40
DVD_MAX = 15
GAME_MAX = 25
BOOK_DISCOUNT = 5
DVD_DISCOUNT = 8
GAME_DISCOUNT = 4

def main():
    book_item_count = get_item_count("books", BOOK_MAX, BOOK_DISCOUNT)
    book_total = get_item_total(book_item_count, BOOK_PRICE, BOOK_DISCOUNT)
    dvd_item_count = get_item_count("DVDs", DVD_MAX, DVD_DISCOUNT)
    dvd_total = get_item_total(dvd_item_count, DVD_PRICE, DVD_DISCOUNT)
    game_item_count = get_item_count("games", GAME_MAX, GAME_DISCOUNT)
    game_total = get_item_total(game_item_count, GAME_PRICE, GAME_DISCOUNT)

    calc_and_display_receipt(book_total, dvd_total, game_total)


# Call the main function.
main()
