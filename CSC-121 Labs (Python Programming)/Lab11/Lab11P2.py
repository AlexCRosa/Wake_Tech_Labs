#
# Alex Cesar Rosa
# 4/3/2024
# Classes and OO Programming - Problem 2
#
import pickle
from inventory_item import InventoryItem, CATEGORY_LIST


def main():
    inventory = load_inventory()
    display_inventory(inventory)

    answer = ''
    while answer.lower() != 'n':
        # TODO - Create an InventoryItem object, ask the user for item input
        #  using the object's method, then append the object to the inventory
        #  list.
        new_item = InventoryItem()
        new_item.get_item_input()

        inventory.append(new_item)

        answer = input('Do you want to enter more items? ')

    for category in CATEGORY_LIST:
        display_category(category, inventory)

    display_inventory(inventory)
    save_inventory(inventory)


def load_inventory():
    inventory = []
    # TODO - Attempt to load inventory data from a binary file named
    #  inventory.dat. If the file exists, load it into the inventory list.
    #  If the file does not exist, leave the inventory list empty.
    try:
        inventory_file = open("inventory.dat", "rb")
        inventory = pickle.load(inventory_file)
        inventory_file.close()
    except FileNotFoundError:
        inventory = []

    return inventory


def save_inventory(inventory):
    # TODO - Open a binary file named inventory.dat and dump the inventory
    #  list that has been passed in as a parameter to that file.
    inventory_file = open("inventory.dat", "wb")
    pickle.dump(inventory, inventory_file)
    inventory_file.close()
    print('Inventory was saved in inventory.dat.')


def display_category(category_name, inventory):
    print()
    header = f'Items in {category_name}'
    divider = len(header) * '-'
    print(header)
    print(divider)
    # TODO - Display inventory items that are in the specific category
    #  Both the category name and inventory are passed in as parameters.
    #  If there are no items in the category, print "No items."
    has_item = False
    for item in inventory:
        if item.category == category_name:
            has_item = True
            print(item)
        else:
            continue

    # Dealing with categories that has no items
    if has_item:
        pass
    else:
        print("No items.")


def display_inventory(inventory):
    print()
    print('Current Inventory')
    print('-----------------')
    # TODO - Display the inventory items that are in the inventory list
    #  that was passed in as a parameter. If the list is empty, display
    #  "Inventory is empty."
    if len(inventory) > 0:
        for item in inventory:
            print(item)
    else:
        print("Inventory is empty.")

    print('-----------------')
    print()

main()
