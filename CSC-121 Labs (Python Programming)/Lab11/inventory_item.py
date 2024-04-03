#
# Alex Cesar Rosa
# 4/3/2024
# That program is intended to hold a class for
# inventory items at Trish's bookstore
#

CATEGORY_LIST = ["Book", "DVD", "Game"]


class InventoryItem:
    def __init__(self, name="", count=0, cost=0.00, category=""):
        self.name = name
        self.count = count
        self.cost = cost
        self.category = category

    def get_item_input(self):
        self.name = input("Enter the item name: ")

        # Get item count
        while True:
            try:
                item_count = int(input('Enter the item count: '))
                if item_count > 0:
                    self.count = item_count
                else:
                    print('Item count must be greater than zero.')
            except ValueError:
                print('Item count must be an integer.')

        # Get unit cost
        while True:
            try:
                unit_cost = float(input('Enter the unit cost: '))
                if unit_cost <= 0:
                    print('Unit cost must be greater than zero.')
                else:
                    self.cost = unit_cost
            except ValueError:
                print('Unit cost must be an integer or float.')

        # Get category
        while True:
            category = input('Enter the category: ')
            if category not in CATEGORY_LIST:
                print(f"{category} not in list of categories: {CATEGORY_LIST}")
            else:
                self.category = category

    def __str__(self):
        if len(self.name) != 0:
            return f"{self.name}\n\tCount: {self.count}, Cost: {self.cost:.2f}\n\tCategory: {self.category}"
        else:
            return "Inventory is empty."
