#
# Alex Cesar Rosa
# 2/7/2024
# This program works on creating and manipulating lists
#

import random


def main():

    # Step A
    print("Step a: ", end="")
    list_length = int(input("How many numbers in each list? "))

    # Step B
    print("Step b:")
    lower_bound = int(input("What is the lower bound for the random number? "))
    upper_bound = int(input("What is the upper bound for the random numbers? "))

    # list creation
    first_list = list_generator(lower_bound, upper_bound, list_length)
    second_list = list_generator(lower_bound, upper_bound, list_length)

    # Step C
    print("Step c: ", end="")
    print(f"First list: {first_list}")

    # Step D
    print("Step d: ", end="")
    print(f"Second list: {second_list}")

    # Step E
    print("Step e:")
    for i in range(list_length):
        print(first_list[i], end=" ")
        print(second_list[i])

    # Step F
    combined_list = first_list + second_list
    print("Step f: ", end="")
    print(f"Combined list: {combined_list}")

    # Step G
    combined_list.sort()
    print("Step g: ", end="")
    print(f"Sorted list: {combined_list}")

    # Step H
    print("Step h:")
    print(f"First three elements: {combined_list[:3]}")
    print(f"Last three elements: {combined_list[-3:]}")

    # Step I
    print("Step i: ", end="")
    print(f"Sum: {sum(combined_list)}")

    # Step J
    print("Step j: ", end="")
    print(f"Minimum: {min(combined_list)}")

    # Step K
    print("Step k: ", end="")
    print(f"Maximum: {max(combined_list)}")

    # Step L
    print("Step l:")
    for i in range(list_length):
        num = random.randint(lower_bound, upper_bound)
        if num in combined_list:
            print(f"{num} at index {combined_list.index(num)}")
            combined_list.remove(num)
        else:
            print(f"{num} not found in list")

    # Step M
    print("Step m: ", end="")
    print(f"Final list: {combined_list}")


def list_generator(lower_bound, upper_bound, list_length):
    nums = []
    for i in range(list_length):
        num = random.randint(lower_bound, upper_bound)
        nums.append(num)

    return nums


main()