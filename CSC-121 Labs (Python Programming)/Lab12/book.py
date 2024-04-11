#
# Alex Cesar Rosa
# 4/14/2024
# That program will hold a subclass for books
#

from inventory_item import InventoryItem


class Book(InventoryItem):
    def __init__(self, item_name="", item_count=0, unit_cost=0.0, item_isbn13=""):
        super().__init__(item_name, item_count, unit_cost, "Book")
        self.isbn13 = item_isbn13

    def get_item_input(self):
        super().get_item_input()

        # Get ISBN13
        while True:
            try:
                item_isbn13 = input('What is the ISBN? ')
                if len(item_isbn13) != 13:
                    print('ISBN must be at least 13 digits longer.')
                else:
                    break
            except:
                print('ISBN must be an integer.')

        self.isbn13 = item_isbn13

    def __str__(self):
        return super().__str__() + \
            f'\n\tISBN: {self.isbn13}'
