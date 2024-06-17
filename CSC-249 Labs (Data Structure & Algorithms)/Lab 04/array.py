#
# Alex Cesar Rosa
# 6/18/2024
# Understand and build the Array class
#

"""
File: array.py

An Array is a restricted list whose clients can use
only [], len, iter, str, insert, remove, clear and clone.

To instantiate, use

<variable> = array(<default capacity>, <optional fill value>)

The fill value is None by default.
"""


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
