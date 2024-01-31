#
# Alex Cesar Rosa
# 1/17/2024
# Gift card program for specific customers
#

# Input
subtotal = float(input("Enter the total purchase amount: "))
loyalty_member = input("Is the customer a loyalty program member (y/n): ")

# Processing
tax = subtotal * 0.065
total = subtotal + tax

if loyalty_member == "y" and 50 <= subtotal <= 100:
    gift_card = 15
elif loyalty_member == "y" and subtotal > 100:
    gift_card = 25
elif loyalty_member == "n" and subtotal > 100:
    gift_card = 5
else:
    gift_card = 0

# Output
print(f"Sales tax: ${tax:.2f}")
print(f"Total after tax: ${total:.2f}")
print(f"Gift Card Awarded: ${gift_card}")