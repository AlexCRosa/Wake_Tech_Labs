#
# Group: Smarty Pants
# 7/23/2024
#

"""
File: listbag.py

A list-based implementation of bags
"""


def display_bag_info(action_response=None):
    if action_response is None:
        print("Challenging! Depending on the type of action you decide to perform, a bag becomes a challenging \n"
              "collection to working on. A bag is a type of unordered collection.\n"
              "However, the bag structure used for this info game is a list based approach, so the items will be\n"
              "ordered by the magic of the built-in Python function: 'List'.\n"
              "\nHere are some important information:\n"
              "A bag’s interface derives from thinking about what bags can do in a real-world situation: A bag can \n"
              "contain any objects.")

    elif action_response == "1":
        print("\nThere is no much to do when adding an item to the bag. The item is just added inside the collection.\n"
              "* The place the item was placed does not matter since the bag is a type of unordered collection.")

    elif action_response == "2":
        print("\nThe remove method can be a trick method depending on the approach for searching the element. Because\n" 
              "of the bag is not sorted, finding an item can consume a lot of time depending on the size of the bag.")

    elif action_response == "3":
        print("\nThe action of checking the length of a bag may be hard depending on the used approach when creating\n"
              "the bag. Taking advantage of the array collection may be a good decision since you keep track of the\n"
              "logical size as you add or remove items.\n")


def bag_actions(initial_bag, action_response):
    if action_response == "1":
        element = int(input("What element do you want to add? "))
        initial_bag.add(element)

    elif action_response == "2":
        element = int(input("What element do you want to remove? "))
        initial_bag.remove(element)

    elif action_response == "3":
        print(f"\nThe bag has {len(initial_bag)} elements.")
    elif action_response == "4":
        print(f"\n{initial_bag}")
    elif action_response == "5":
        initial_bag.clear()

    return initial_bag


class ListBag(object):

    # Constructor
    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self.items = list()

        if sourceCollection:
            for item in sourceCollection:
                self.items.append(item)

    # Accessor methods
    def isEmpty(self):
        """Returns True if the bag is empty, or False otherwise."""
        return len(self.items) == 0

    def __len__(self):
        """Returns the number of items in self."""
        return len(self.items)

    def __str__(self):
        """Returns the string representation of self."""
        temp = str(self.items)[1:-1]
        return "{" + temp + "}"

    def __iter__(self):
        """Supports iteration over a view of self."""
        for item in self.items:
            yield item

    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""
        new_bag = self.items
        for item in other:
            new_bag.append(item)
        return ListBag(new_bag)

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if isinstance(other, ListBag):
            return self.items == other.items
        return False

    def count(self, item):
        """Returns the number of instances of item in self."""
        return self.items.count(item)

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.items = list()

    def add(self, item):
        """Adds item to self."""
        self.items.append(item)

    def remove(self, item):
        """Remove item from self.
        Raises KeyError if item is not in self."""
        try:
            self.items.remove(item)
        except ValueError:
            return f"{item} is not in bag."
