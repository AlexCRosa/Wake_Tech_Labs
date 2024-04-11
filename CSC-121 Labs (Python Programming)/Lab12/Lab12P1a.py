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
    obj1 = Book("Python Now", 100, 22.95, "2345234523451")
    obj2 = Book("Even More Python", 150, 8.95, "3456345634561")
    obj3 = Game("Uno", 75, 6.5, "123456789012")
    obj4 = DVD("Barbie", 50, 12.00, "098765432121", "Comedy")
    obj5 = DVD("The Piano", 10, 2.90, "321321321321", "Drama")

    print(obj1)
    print(obj2)
    print(obj3)
    print(obj4)
    print(obj5)


main()
