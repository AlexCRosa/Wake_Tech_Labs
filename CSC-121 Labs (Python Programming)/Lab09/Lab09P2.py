#
# Alex Rosa
# 3/20/2024
# Creating and managing sets
#

def main():
    import random

    set1 = {random.randint(1, 16) for i in range(8)}
    set2 = {random.randint(1, 16) for i in range(8)}

    print(f"set1: {set1}")
    print(f"set2: {set2}")

    # union
    new_set = set1 | set2
    print(f"Union of set1 and set2: {new_set}")

    # intersection
    intersection_set = set1 & set2
    print(f"Intersection of set1 and set2: {intersection_set}")

    # difference
    differences_set = set1 - set2
    print(f"Difference of set1 and set2: {differences_set}")

    # symmetric difference
    symmetric_set = set1 ^ set2
    print(f"Symmetric difference of set1 and set2: {symmetric_set}")

    # Less than 10
    less_than_ten = {i for i in new_set if i < 10}
    print(f"Less than 10 in union of set1 and set2: {less_than_ten}")


main()
