#
# Alex Cesar Rosa
# 5/28/2024
#

amount_copies = int(input("How many copies are you buying? "))

# Display the unit price based on the amount of copies
if amount_copies <= 10:
    print("Unit price: $99")
    total = amount_copies * 99
elif amount_copies <= 50:
    print("Unit price: $89")
    total = amount_copies * 89
elif amount_copies <= 100:
    print("Unit price: $79")
    total = amount_copies * 79
else:
    print("Unit price: $69")
    total = amount_copies * 69

# Display the total
print(f"Total price: ${total}")
