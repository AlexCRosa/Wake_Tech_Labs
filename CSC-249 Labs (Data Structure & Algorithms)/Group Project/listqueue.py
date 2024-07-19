#
# Group: Smarty Pants
# 7/23/2024
#

"""
File: listqueue.py
A list-based implementation of stacks.
"""


def display_queue_info(action_response=None):
    if action_response is None:
        print("\nGood! Queues are linear collections, and there are several implementation strategies for queues - \n"
              "some based on arrays, and others based on linked structures.\n\n"
              
              "Queues are omnipresent in everyday life and occur in any situation where people or things are lined\n"
              "up for service or processing on a first-come, first-served basis.")

    elif action_response == "1":
        print("\nThe operation of adding an item to the queue is called 'add', and the added item will always be\n"
              "placed after the last item of the queue. The end of the queue is called 'rear'.")

    elif action_response == "2":
        print("\nA queue supports a first-in first-out (FIFO) protocol.\n"
              "Checkout lines in stores and airport check-in lines are familiar examples of queues.\n"
              "The operation for removing items from a queue is called 'pop'. Every time a item is popped from the\n"
              "queue, the first item of the queue is removed.")


def queue_actions(initial_queue, action_response):
    if action_response == "1":
        element = int(input("What element do you want to add? "))
        initial_queue.add(element)

    elif action_response == "2":
        initial_queue.pop()

    elif action_response == "3":
        print(f"\nThe queue has {len(initial_queue)} elements.")
    elif action_response == "4":
        print(f"\n{initial_queue}")
    elif action_response == "5":
        initial_queue.clear()

    return initial_queue


class ListQueue(object):

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self.items = list()

        if sourceCollection:
            for item in sourceCollection:
                self.items.append(item)

    # Accessor methods
    def isEmpty(self):
        """Returns True if the queue is empty, or False otherwise."""
        return len(self.items) == 0
    
    def __len__(self):
        """Returns the number of items in the queue."""
        return len(self.items)

    def __str__(self):
        """Returns the string representation of the queue."""
        temp = str(self.items)[1:-1]
        return "{" + temp + "}"

    def __iter__(self):
        """Supports iteration over a view of the queue."""
        for item in self.items:
            yield item

    def __add__(self, other):
        """Returns a new queue containing the contents
        of self and other."""
        new_queue = self.items
        for item in other:
            new_queue.append(item)
        return ListQueue(new_queue)

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if isinstance(other, ListQueue):
            return self.items == other.items
        return False

    def peek(self):
        """Returns the item at the front of the queue.
        Raises IndexError if queue is not empty."""
        if self.isEmpty():
            raise IndexError("Queue is empty")
        return self.items[0]

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.items = list()

    def add(self, item):
        """Inserts item at the rear of the queue."""
        self.items.append(item)

    def pop(self):
        """Removes and returns the item at the front of the
        queue. Raises IndexError if queue is not empty."""
        if self.isEmpty():
            raise IndexError("Queue is empty")

        old_item = self.items[0]
        self.items.pop(0)

        return old_item
