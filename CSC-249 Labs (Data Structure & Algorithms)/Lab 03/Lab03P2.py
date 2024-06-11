#
# Alex Cesar Rosa
# 6/11/2024
# Counting Sort
#

def main():
    list1 = [8, 2, 4, 5, 4, 7, 2, 6, 8, 6, 2, 5, 6]
    list1_sorted = counting_sort(list1)
    print("list1 before sorting:", list1)
    print("list1 after sorting:", list1_sorted)


def counting_sort(my_list):
    smallest = min(my_list)
    largest = max(my_list)
    sorted_list = []

    for i in range(smallest, largest + 1):
        count = my_list.count(i)
        sorted_list.extend([i] * count)

    return sorted_list


if __name__ == "__main__":
    main()
