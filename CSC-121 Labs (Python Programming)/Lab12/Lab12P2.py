#
# Student Name
# Date
# Inheritance and Polymorphism - Problem 2
#
import pickle
from inventory_item import InventoryItem
from book import Book
from game import Game
from dvd import DVD


def main():
    # Calling load_inventory() should return a list of inventory items if
    # inventory.dat is present. If that file is not present, it should
    # return an empty list.
    inventory = load_inventory()
    display_inventory(inventory)

    answer_outer = ''
    while answer_outer.lower() != 'n':
        answer_inner = ''
        while answer_inner not in ['1', '2', '3']:
            answer_inner = input('What item type (1-Book, 2-Game, 3-DVD)? ')
            if answer_inner not in ['1', '2', '3']:
                print('Enter 1, 2, or 3.')

        # TODO - Create an appropriate object, ask the user for item input
        #  using the object's method, then append the object to the inventory
        #  list.

        if answer_inner == '1':
            item = Book()
        elif answer_inner == '2':
            item = Game()
        elif answer_inner == '3':
            item = DVD()

        item.get_item_input()
        inventory.append(item)

        answer_outer = input('Do you want to enter more items? ')
        print()

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

    print('Inventory.dat file was created.')


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
