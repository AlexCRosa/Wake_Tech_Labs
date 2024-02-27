#
# Student Name (Replace with your name)
# Assignment Date (Replace with the date)
# Count uppercase letters in a string
#
import os

# DO NOT CHANGE ANY CODE IN THE MAIN FUNCTION
def main():
    try:
        input_file = open('strings.txt', 'r')  # Open a file for reading
        for line in input_file:  # Use a for loop to read each line in the file
            manipulate_text(line)
            print()
    except FileNotFoundError:
        print('Did not find strings.txt in current directory:')
        print(os.getcwd())


def manipulate_text(line):
    # TODO: Delete the following line, then implement the function as indicated
    #  in the problem specification
    print(line)


main()
