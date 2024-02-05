#
# Instructor solution
# 8/2/2023
# Module to help process item data
#

# Global Constants - Use these in your program where it makes sense
TAX_RATE = 0.065  # 6% sales tax
VOLUME_DISCOUNT = 0.95  # 95% of total is 5% off

# The get_item_count function takes three parameters:
#    item_name - Name of item being prompted about
#    max_allowed - Maximum number of items the user can enter
#    discount_threshold - Minimum number of items eligible for 5% discount
#
# This function will ask the user to enter the number of items and
# validate the number entered is between 0 and the max_allowed
# inclusive. The number of items the user enters is returned.
def get_item_count(item_name, max_allowed, discount_threshold):
    print(f'Enter the number of {item_name}.')
    items = int(input(f'\t{discount_threshold} or more receive a discount: '))

    # TODO: Add the input validation code here
    while not 0 <= items <= max_allowed:
        print(f"Number of items must be between 0 and {max_allowed}")
        items = int(input("Enter the number of books: "))

    return items

# The get_item_total function takes two parameters:
#     num_items - Number of items
#     unit_price - The cost of each item
#     discount_threshold - Minimum number of items eligible for 5% discount
#
# This function calculates the total cost for the items and
# returns that value.
def get_item_total(num_items, unit_price, discount_threshold):
    # TODO: Remove the following pass statement, then implement
    #  this function.
    item_total_cost = num_items * unit_price

    # Check if the discount is applied
    if num_items >= discount_threshold:
        item_total_cost = item_total_cost - 0.05
        return item_total_cost
    else:
        return item_total_cost

# The calc_and_display_receipt function will calculate all the
# necessary values and display the receipt. It takes three parameters:
#    book_total - Total cost of books
#    dvd_total - Total cost of DVDs
#    game_total  - Total cost of games
#
# This function will calculate total before tax, the tax on the total,
# and the total after tax is added.
#
# The receipt should display the total cost of books, DVDs, and
# games IF the item cost is greater than 0. The receipt should also
# include the subtotal, tax, and total.
def calc_and_display_receipt(book_total, dvd_total, game_total):
    # TODO: Remove the following pass statement, then implement
    #  this function.
    pass