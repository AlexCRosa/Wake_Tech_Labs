#
# Alex Cesar Rosa
# 6/11/2024
# Finding second largest item in a list
#

def main():
    list1 = [2, 8, 7, 5, 4, 1, 6]
    second_largest = find_second_largest(list1)
    print("list1:", list1)
    print("Second largest item in list1:", second_largest)
    print()
    list2 = [2, 8, 8, 5, 4, 1, 6]
    second_largest = find_second_largest(list2)
    print("list1:", list2)
    print("Second largest item in list2:", second_largest)


def find_second_largest(my_list):
    temp_list = my_list.copy()
    max_num = 0

    for i in temp_list:
        if i > max_num:
            max_num = i
        else:
            continue

    temp_list.remove(max_num)
    max_num = 0

    for i in temp_list:
        if i > max_num:
            max_num = i
        else:
            continue

    return max_num


if __name__ == "__main__":
    main()
