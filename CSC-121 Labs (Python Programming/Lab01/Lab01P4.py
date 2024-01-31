#
# Alex Rosa
# 1/10/2024
# This program was created to calculate the final price of a purchase.
#

# Input
book_order = int(input("Enter the number of books: "))
dvd_order = int(input("Enter the number of DVDs: "))
games_order = int(input("Enter the number of games: "))

# Processing
cost_before_tax = float((book_order * 2.25) + (dvd_order * 4.35) + (games_order * 5.00))
tax_cost = float(cost_before_tax * 0.065)
cost_after_tax = cost_before_tax + tax_cost

# Output
print(f"Cost before tax: {cost_before_tax:.2f}")
print(f"Sales tax: {tax_cost:.2f}")
print(f"Cost after tax: {cost_after_tax:.2f}")
