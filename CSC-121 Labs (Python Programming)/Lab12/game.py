#
# Alex Cesar Rosa
# 4/14/2024
# That program will hold a subclass for games
#

from inventory_item import InventoryItem


class Game(InventoryItem):
    def __init__(self, item_name="", item_count=0, unit_cost=0.0, item_upc=""):
        super().__init__(item_name, item_count, unit_cost, "Game")
        self.upc = item_upc

    def get_item_input(self):
        super().get_item_input()
        # Get UPC
        while True:
            try:
                item_upc = input('What is the UPC? ')
                if len(item_upc) != 12:
                    print('UPC must be at least 12 digits longer.')
                else:
                    break
            except:
                print('UPC must be an integer.')

        self.upc = item_upc

    def __str__(self):
        return super().__str__() + \
            f'\n\tUPC: {self.upc}'
