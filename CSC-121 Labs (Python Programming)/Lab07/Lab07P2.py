#
# Alex Cesar Rosa
# 2/28/2024
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
    NAME = "Alex"
    EMAIL = "acrosa@my.waketech.edu"
    CITY = "Apex"

    line = line.strip()
    print(line)
    line = line.replace("$NAME", NAME)
    line = line.replace("$EMAIL", EMAIL)
    line = line.replace("$CITY", CITY)
    print(f"Updated line: {line}")
    print(f"Number of characters in updated line: {len(line)}")

    count = 0
    tmp_string = line.split()
    tmp_string = line.split(",")
    print(f"That is the new variable {tmp_string}")
    for i in tmp_string:
        if i == "Alex":
            count += 1
    print(f"Occurrences of '{NAME}': {count}")


main()
