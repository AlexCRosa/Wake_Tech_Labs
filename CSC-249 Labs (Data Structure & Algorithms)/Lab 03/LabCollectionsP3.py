#
# Alex Cesar Rosa
# 6/11/2024
#

import random


def main():
    set1 = set_generator()
    set2 = set_generator()

    print(f"set1: {set1}")
    print(f"set2: {set2}")

    # Union of sets
    print(f"Union of set1 and set2: {set1 | set2}")

    # Intersection of sets
    print(f"Intersection of set1 and set2: {set1 & set2}")

    # Symmetric difference between sets
    print(f"Symmetric difference between set1 and set2: {set1 ^ set2}")


def set_generator():
    set_to_export = set()

    for i in range(5):
        num = random.randint(1, 10)
        set_to_export.add(num)

    return set_to_export


if __name__ == '__main__':
    main()