#
# Alex Cesar Rosa
# 4/14/2024
# That program will process and hold information within the
# superclasses and subclasses from the directory
#

from inventory_item import InventoryItem
from book import Book
from game import Game
from dvd import DVD


def main():
    tmp_list = []

    for i in range(3):
        choice = ""
        while choice not in ["1", "2", "3"]:
            choice = input("What item type (1-Book, 2-Game, 3-DVD)? ")
            if choice == '1':
                item = Book()
            elif choice == '2':
                item = Game()
            elif choice == '3':
                item = DVD()
            else:
                print('Enter 1, 2, or 3.')

        item.get_item_input()
        tmp_list.append(item)

    for i in tmp_list:
        print(i)

main()
