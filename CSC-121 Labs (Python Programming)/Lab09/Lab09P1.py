#
# Alex Rosa
# 3/18/2024
# Word counting in dictionaries
#

# DO NOT UPDATE ANY PART OF THE MAIN FUNCTION
def main():
    input_file = open('words.txt', 'r')  # Open a file for reading
    file_text = input_file.read().upper()  # Read all contents and convert to uppercase
    process_file(file_text)
    input_file.close()


def process_file(text):
    # TODO: Create an empty dictionary
    new_dict = {}

    # TODO: Use the split method to get a list of words from the input parameter
    tmp = text.split()

    # TODO: Use a for loop to go through the list 1-by-1
    #  and count the occurrence of each word. Add or update
    #  the entries in the dictionary with the word/count pairs.
    for idx in tmp:
        if idx not in new_dict:
            new_dict[idx] = 1
        elif idx in new_dict:
            new_dict[idx] += 1

    # TODO: Print the dictionary
    print(new_dict)

    # TODO: Create a list of words with the maximum count
    #  and print the list.
    max_count_list = []
    num_max = 0

    for value in new_dict.values():
        if value >= num_max:
            num_max = value
        else:
            continue

    for key, value in new_dict.items():
        if value == num_max:
            max_count_list.append(key)

    print(f"Words with max count of 4: {max_count_list}")

    # TODO: Remove the words with max count from the dictionary
    #  and print the dictionary.
    for i in max_count_list:
        del (new_dict[i])

    print(f"Dictionary with max removed: {new_dict}")

    # TODO: Put all the words in the dictionary in a list, sort it,
    #  and print the list of sorted words.
    new_list = []
    for key in new_dict.keys():
        new_list.append(key)

    new_list.sort()
    print(f"Words sorted: {new_list}")


main()
