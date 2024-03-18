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
    print(tmp)
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

    # TODO: Remove the words with max count from the dictionary
    #  and print the dictionary.

    # TODO: Put all the words in the dictionary in a list, sort it,
    #  and print the list of sorted words.

    pass  # TODO: Remove this line before submitting to BB.

main()
