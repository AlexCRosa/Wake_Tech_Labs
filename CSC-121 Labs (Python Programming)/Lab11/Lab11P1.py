#
# Alex Cesar Rosa
# 4/3/2024
# That program is intended to manage inventory items at Trish's bookstore
#

from inventory_item import InventoryItem


def main():
    # Creating the three starter objects
    item1 = InventoryItem("Python for All", 10, 12.95, "Book")
    item2 = InventoryItem("Barbie", 15, 6.95, "DVD")
    item3 = InventoryItem("Uno", 32, 4.50, "Game")

    # Print the three objects created
    print(item1)
    print(item2)
    print(item3)
    print()

    # Create a new InventoryItem by asking the user for item's information
    new_item = InventoryItem()
    new_item.get_item_input()

    # Print the new item
    print()
    print(new_item)


main()
