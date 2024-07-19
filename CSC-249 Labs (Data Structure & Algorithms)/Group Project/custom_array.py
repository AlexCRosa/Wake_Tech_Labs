#
# Alex Cesar Rosa
# 6/18/2024
# Understand and build the Array class
#

"""
File: custom_array.py

An Array is a restricted list whose clients can use
only [], len, iter, str, insert, remove, clear and clone.

To instantiate, use

<variable> = array(<default capacity>, <optional fill value>)

The fill value is None by default.
"""


def display_array_info(action_response=None):
    if action_response is None:
        print("\nCool! Array is one of the most famous type of collection among programmers.\n\n"
              "Here are some important information:\n"
              "1.	Array represents a sequence of items that can be accessed or replaced at given index positions.\n"
              "2.	Each element of an array is called an item. You can access each item by providing its index.\n"
              "3.	Every array is created with a reasonable default size at program start-up. When the array cannot \n"
              "hold more data, create a new, larger array and transfer the data items from the old array. When the \n"
              "array seems to be wasting memory, decrease its length in a similar manner.")

    elif action_response == "1":
        print("\nIn the case of insertion a target index and the new item must be provided:\n" 
              "1. Check for available space before attempting an insertion and increase the physical size of the \n"
              "array, if necessary.\n"
              "2. Shift the items from the logical end of the array to the target index position down by one. (This \n"
              "process opens a hole for the new item at the target index)\n"
              "3. Assign the new item to the target index position.\n"
              "4. Increment the logical size by one")

    elif action_response == "2":
        print("\nIn the case of removing:\n"
              "1. Shift the items from the one following the target index position to the logical end of the array \n" 
              "up by one. This process closes the hole left by the removed item at the target index.\n"
              "2. Decrement the logical size by one"
              "3. Decrease the physical size of the array, if necessary.")

    elif action_response == "3":
        print("\nIf you have already interacted with the array, you should notice that the size of the array may have\n"
              "changed. It happens because if the array gets full, it will automatically increase its size. The \n"
              "array will also decrease its size when you start removing items.\n")


def array_actions(initial_array, action_response):
    if action_response == "1":
        element_position = int(input("Please specify the index to add the item? "))
        element = int(input("What item do you want to add? "))
        initial_array.insert(element_position, element)

    elif action_response == "2":
        element = int(input("Please provide the index of the item you want to remove? "))
        initial_array.remove(element)

    elif action_response == "3":
        print(f"\nThe array has {len(initial_array)} elements.")
    elif action_response == "4":
        print(f"\n{initial_array}")
    elif action_response == "5":
        initial_array.clear()

    return initial_array


class Array(object):
    """Represents an array."""

    def __init__(self, capacity, fillValue=None):
        """Capacity is the static size of the array.
        fillValue is placed at each position."""
        self.items = list()
        self.logicalSize = 0
        # Track the capacity and fill value for adjustments later
        self.capacity = capacity  # default capacity of the array
        self.fillValue = fillValue
        for count in range(capacity):
            self.items.append(fillValue)

    def __len__(self):
        """-> The capacity of the array."""
        return len(self.items)

    def __str__(self):
        """-> The string representation of the array."""
        return str(self.items)

    def __iter__(self):
        """Supports traversal with a for loop."""
        return iter(self.items)

    def __getitem__(self, index):
        """Subscript operator for access at index.
        Precondition: 0 <= index < size()"""
        if index < 0 or index >= self.size():
            raise IndexError("Array index out of bounds")
        return self.items[index]

    def __setitem__(self, index, newItem):
        """Subscript operator for replacement at index.
        Precondition: 0 <= index < size()"""
        if index < 0 or index >= self.size():
            raise IndexError("Array index out of bounds")
        self.items[index] = newItem

    def size(self):
        """-> The number of items in the array."""
        return self.logicalSize

    def __grow(self):
        """Increases the physical size of the array if necessary."""
        # Double the physical size if no more room for items
        # and add the fillValue to the new cells in the underlying list
        for count in range(len(self)):
            self.items.append(self.fillValue)

    def __shrink(self):
        """Decreases the physical size of the array if necessary."""
        # Shrink the size by half but not below the default capacity
        # and remove those garbage cells from the underlying list
        newSize = max(self.capacity, len(self) // 2)
        for count in range(len(self) - newSize):
            self.items.pop()

    def insert(self, index, newItem):
        """Inserts item at index in the array."""
        if index < 0:
            index = 0
        elif index > self.logicalSize:
            index = self.logicalSize

        if self.logicalSize == self.capacity:
            self.__grow()

        for i in range(self.logicalSize, index, -1):
            self.items[i] = self.items[i - 1]

        self.items[index] = newItem
        self.logicalSize += 1

    def remove(self, index):
        """Removes and returns item at index in the array."""
        try:
            for i in range(index, self.logicalSize - 1):
                self.items[i] = self.items[i + 1]
                self.items[i + 1] = self.fillValue
            self.logicalSize -= 1
        except IndexError:
            print("Array index out of bounds")

        if self.logicalSize < (len(self.items) * 0.25) and len(self.items) >= self.capacity * 2:
            self.__shrink()

    def clear(self):
        """Removes all data items and resets the array to default."""
        self.items = [self.fillValue] * self.capacity
        self.logicalSize = 0

    def clone(self):
        """Creates and returns a clone of this Array object."""
        clonedArray = Array(self.capacity, self.fillValue)
        clonedArray.items = self.items
        clonedArray.logicalSize = self.logicalSize
        return clonedArray


def main():
    """Test code for modified Array class."""
    a = Array(5)
    print("Initial array:", a)
    for item in range(4):
        a.insert(0, item)
    print("Insert 3, 2, 1, 0:", a)
    a.insert(1, 77)
    print("Insert 77 at index 1:", a)
    a.insert(2, 88)
    print("Insert 88 at index 2:", a)
    a.insert(15, 10)
    print("Insert 10 at index 15:", a)
    a.insert(-1, 66)
    print("Insert 66 at index -1:", a)
    a.remove(3)
    print("Remove item at index 3:", a)
    for count in range(5):
        a.remove(0)
        print("Remove item at index 0:", a)
    b = a.clone()
    print("clone created:", b)
    b.clear()
    print("clone cleared:", b)


if __name__ == "__main__":
    main()
