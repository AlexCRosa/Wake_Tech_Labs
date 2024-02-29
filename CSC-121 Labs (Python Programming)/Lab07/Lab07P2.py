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

    # Counting the occurrences of NAME
    count = 0
    tmp_string = line.split()
    for i in tmp_string:
        if i.startswith(NAME):
            count += 1
    print(f"Occurrences of '{NAME}': {count}")

    print(f"First half of line: {line[:(int(len(line)//2))]}")
    print(f"Second half of line: {line[(int(len(line)//2)):]}")

    print(f"Line in uppercase: {line.upper()}")
    print(f"Line in lowercase: {line.lower()}")

main()
