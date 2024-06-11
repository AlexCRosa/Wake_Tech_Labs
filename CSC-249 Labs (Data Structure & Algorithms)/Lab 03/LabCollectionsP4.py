#
# Alex Cesar Rosa
# 6/11/2024
#

def main():
    user_string = input("Enter a string: ").upper()
    print()
    string_list = string_manager(user_string)

    dictionary = dictionary_creator(string_list)
    print(f"Dictionary: {dictionary}")

    user_letter = input("Choose a letter: ").upper()
    print(f"Frequency count of that letter: {dictionary[user_letter]}")

    del dictionary[user_letter]
    print(f"Dictionary after that letter removed: {dictionary}")

    dictionary_list = list(dictionary.keys())
    print(f"Letters sorted: {sorted(dictionary_list)}")


def string_manager(user_string):
    """ Convert user_string into a list with only alphabet letters """
    list_to_export = list()

    for i in user_string:
        if i.isalpha():
            list_to_export.append(i)
        else:
            continue

    return list_to_export


def dictionary_creator(string_list):
    """ Count and create a dictionary from the string_list """
    dictionary_to_export = dict()

    for i in string_list:
        if i in dictionary_to_export.keys():
            dictionary_to_export[i] += 1
        else:
            dictionary_to_export[i] = 1

    return dictionary_to_export


if __name__ == '__main__':
    main()
