#
# Instructor Provided File
# 3/23/2024
# Inheritance and Polymorphism - Problem 1 & 2
#
# Students: DO NOT CHANGE THIS FILE. Use it as the base class
# for your Book, Game, and DVD classes

class InventoryItem:
    def __init__(self, item_name, item_count, unit_cost, item_category):
        self.name = item_name
        self.count = item_count
        self.cost = unit_cost
        self.category = item_category

    # For get_item_input(), we will not be asking the user to
    # enter a category. That category will be filled in by the
    # subclasses that use this base class.
    def get_item_input(self):
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
            except:
                print('Item count must be an integer.')
        # Get unit cost
        while True:
            try:
                unit_cost = float(input('Enter the unit cost: '))
                if unit_cost < 0:
                    print('Unit cost must be 0 or greater.')
                else:
                    break
            except:
                print('Unit cost must be an integer.')

        self.name = item_name
        self.count = item_count
        self.cost = unit_cost

    def __str__(self):
        return f'{self.name}\n' + \
            f'\tCount: {self.count}, Cost: {self.cost:.2f}\n' + \
            f'\tCategory: {self.category}'
