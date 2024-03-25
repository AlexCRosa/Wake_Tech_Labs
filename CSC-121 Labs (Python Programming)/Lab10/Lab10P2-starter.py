#
# Student Name
# Date
# Starter Code for Lab 10 Problem 2 (Remove this line before submitting)
# Trish's Bookstore Inventory System
#
import pickle
CATEGORY_LIST = ['Book', 'DVD', 'Game']

# Review the main() function and update TODO sections.
# Do not change any other code within main().
def main():
    inventory_counts, inventory_costs, inventory_categories = read_inventory_file()

    print("Welcome to Trish's Inventory Input System")
    print("Current Inventory:")
    display_all_inventory(inventory_counts, inventory_costs, inventory_categories)

    response = ''
    while response != '0':
        display_menu()
        response = input('Enter your choice: ')

        if response == "1":  # Add an item
            item_name, item_count, unit_cost, category = get_item_input()
            # TODO - Replace pass with code that will add the item_name,
            #  item_count, and unit_cost data to the dictionaries
            pass
        elif response == "2":  # Display a single item
            item_name = input('Enter item name: ')
            # TODO - Replace pass with code that will display the item data
            #  from the dictionaries or display "Not found"
            pass
        elif response == "3":  # Display items in a category
            category_name = input('Enter category name: ')
            print(f'\nItems in {category_name}:')
            if category_name in CATEGORY_LIST:
                # TODO - Replace pass with code that will print the names
                #  of all the items in the category
                pass
            else:
                print(f'{category_name} not in list of categories: {CATEGORY_LIST}')
        elif response == "4":  # Delete a single item
            item_name = input('Enter item name: ')
            # TODO - Replace pass with code that will remove the item data
            #  from the dictionaries or display "Not found"
            pass
        elif response == "5":  # Display all inventory
            # TODO - Replace pass with code that will display all the inventory
            #  items - HINT Don't we already have a function that does that?
            pass
        elif response != "0":
            print("Invalid choice. Try again.\n")
        print()

    # Ready to exit the program, display and save inventory as last steps
    print("Final Inventory:")
    display_all_inventory(inventory_counts, inventory_costs, inventory_categories)

    save_inventory_file(inventory_counts, inventory_costs, inventory_categories)


def display_menu():
    print("What would you like to do?")
    print("(1) Add an item\n"
          "(2) Display an item\n"
          "(3) Display a category\n"
          "(4) Delete an item\n"
          "(5) Display all inventory\n"
          "(0) Exit")


def display_all_inventory(inventory_counts, inventory_costs, inventory_categories):
    # TODO - Replace pass with code that will iterate through the dictionaries
    #  that are passed in and display the inventory. If the dictionaries are
    #  empty the display "== Empty =="
    pass


def save_inventory_file(inventory_counts, inventory_costs, inventory_categories):
    # TODO - Replace pass with code that will save your dictionaries to
    #  inventory.dat using the pickle module.
    pass


def read_inventory_file():
    inventory_counts = {}
    inventory_costs = {}
    inventory_categories = {}
    # TODO - Replace pass with code that will read your dictionaries from
    #  inventory.dat using the pickle module.
    pass
    return inventory_counts, inventory_costs, inventory_categories


# This function is complete, no changes needed, but feel free to review
def get_item_input():
    # Get item name
    item_name = input('Enter the item name: ')
    # Get item count
    while True:
        try:
            item_count = int(input('Enter the item count: '))
            if item_count < 0:
                print('Item count must be 0 or greater.')
            else:
                break
        except ValueError:
            print('Item count must be an integer.')
    # Get unit cost
    while True:
        try:
            unit_cost = float(input('Enter the unit cost: '))
            if unit_cost < 0:
                print('Unit cost must be 0 or greater.')
            else:
                break
        except ValueError:
            print('Unit cost must be an integer.')
    # Get category
    while True:
        category = input('Enter the category: ')
        if category not in CATEGORY_LIST:
            print(f'Category must be in this list: {CATEGORY_LIST}')
        else:
            break
    return item_name, item_count, unit_cost, category


main()
