#
# Alex Cesar Rosa
# 2/14/2024
# This program tests the student understanding of list comprehensions
#
def main():
    # Step A
    list1 = [4, 5, 8, 2]
    list2 = [2, 5, 9]

    # Step B
    list3 = [num * 2 - 3 for num in range(6)]
    print(f"Step b: {list3}")

    # Step C
    list4 = [[i, j] for i in range(4) for j in range(5) if i % 2 == 1 and j % 2 == 0]
    print(f"Step c: {list4}")

    # Step D
    list5 = [i ** 3 for i in list1]
    print(f"Step d: {list5}")

    # Step E
    list6 = [i * 3 for i in list1]
    print(f"Step e: {list6}")

    # Step F
    list7 = [i * j - 1 for i in list1 for j in list2]
    print(f"Step f: {list7}")

    # Step G
    list8 = [[str(i) + "@" + str(j)] for i in list1 for j in list2]
    print(f"Step g: {list8}")


main()
