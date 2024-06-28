"""
File: listsortedbag.py

A list-based implementation of sorted bag
"""

from listbag import ListBag


class ListSortedBag(ListBag):

    # Constructor
    def __init__(self, sourceCollection=None):
        """Create a list to store items in ascending order"""
        self.items = list()
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    def __contains__(self, item):
        """Returns True if item is in self, or False
        otherwise. Use binary search"""
        left = 0
        right = len(self) - 1
        visited_items = []
        while left <= right:
            midpoint = (left + right) // 2
            visited_items.append(self.items[midpoint])
            if self.items[midpoint] == item:
                print(f"Items visited: {visited_items}")
                return True
            elif self.items[midpoint] > item:
                right = midpoint - 1
            else:
                left = midpoint + 1
        print(f"Items visited: {visited_items}")
        return False

    def __add__(self, other):
        """Returns a new sorted bag containing the
        contents of self and other."""
        new_bag = ListSortedBag()
        for item in self:
            new_bag.add(item)
        for item in other:
            new_bag.add(item)
        return new_bag

    def add(self, item):
        """Adds item to self."""
        if self.isEmpty():
            self.items.append(item)
            print(f"Item added: {item}  Item added at the front")
        elif item >= self.items[- 1]:
            self.items.append(item)
            print(f"Item added: {item}  Item added at the end.")
        else:
            targetIndex = 0
            visited_items = []

            while targetIndex < len(self.items) and item > self.items[targetIndex]:
                visited_items.append(self.items[targetIndex])
                targetIndex += 1
            else:
                visited_items.append(self.items[targetIndex])

            self.items.append(None)  # Increase the size of the list
            for i in range(len(self.items) - 1, targetIndex, -1):
                self.items[i] = self.items[i - 1]

            self.items[targetIndex] = item
            print(f"Item added: {item}  Items visited: {visited_items}")


def main():
    lyst = [8, 2, 4, 7, 6, 1]
    print("The list of items added is:", lyst)
    b = ListSortedBag(lyst)
    print("The bag's size:", len(b))
    print("The bag's string:", b)
    print()
    print("Searching for 6")
    print("6 is in the bag:", 6 in b)
    print()
    print("Searching for 3")
    print("3 is in the bag:", 3 in b)
    print()
    print("Add 5 in bag")
    b.add(5)
    print("The bag's string:", b)
    print()
    print("c = ListSortedBag(3, 4)")
    c = ListSortedBag([3, 4])
    print()
    print("d = b + c")
    d = b + c
    print("bag d's string:", d)

if __name__ == "__main__":
    main()