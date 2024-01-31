#
# Alex Cesar Rosa
# 1/24/2024
# Validating data entry program
#

# Input
while True:
    book_order = int(input("Enter the number of books: "))
    if book_order < 0 or book_order >= 30:
        print("Number of books must be between 0 and 30.")
    else:
        break

while True:
    dvd_order = int(input("Enter the number of DVDs: "))
    if dvd_order < 0 or dvd_order >= 15:
        print("Number of DVDs must be between 0 and 15.")
    else:
        break

while True:
    games_order = int(input("Enter the number of games: "))
    if games_order < 0 or games_order >= 10:
        print("Number of games must be between 0 and 10.")
    else:
        break

# Processing
cost_before_tax = float((book_order * 2.25) + (dvd_order * 4.35) + (games_order * 5.00))
tax_cost = float(cost_before_tax * 0.065)
cost_after_tax = cost_before_tax + tax_cost

# Output
print(f"Cost before tax: {cost_before_tax:.2f}")
print(f"Sales tax: {tax_cost:.2f}")
print(f"Cost after tax: {cost_after_tax:.2f}")