#
# Alex Cesar Rosa
# 6/11/2024
#

import random


def main():
    main_list = list_generator()
    print(f"Tuple of 10 random numbers: {tuple(main_list)}")

    tuple_a = tuple(main_list[:3])
    print(f"Tuple of first 3 numbers: {tuple_a}")

    tuple_b = tuple(main_list[-3:])
    print(f"Tuple of last 3 numbers: {tuple_b}")

    print(f"Two tuples concatenated: {tuple_a + tuple_b}")

    sorted_tuple = sorted(list(tuple_a + tuple_b))
    print(f"Two tuples concatenated and sorted: {tuple(sorted_tuple)}")


def list_generator():
    list_to_export = list()

    for i in range(10):
        num = random.randint(1, 15)
        list_to_export.append(num)

    return list_to_export


if __name__ == '__main__':
    main()
