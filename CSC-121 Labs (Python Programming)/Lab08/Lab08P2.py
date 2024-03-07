#
# Alex Cesar Rosa
# 3/6/2024
# This program generate a daily sales report that categorizes
# and totals sales for each category of items sold
#

def main():
    # Find and open the file
    try:
        file1 = open("sales.txt", 'r')
    except FileNotFoundError:
        print("File 'sales.txt' not found")
        exit()

    # Counter for keep track of the line numbers
    line_counter = 1

    # Variables to keep the total of the items sold
    books = 0
    dvds = 0
    games = 0

    # Iterate through the file each line at a time
    for line in file1:
        # Receive a list of the line content removing commas and white spaces
        tmp = line.split(", ")

        # The readline method includes a new line argument that need to be removed
        tmp[2] = tmp[2].rstrip("\n")

        # The logic when processing the calculation should be inside
        # the 'try' and 'exception' to handle cases where the price line
        # could not be converted to a float
        try:
            if tmp[1] == "Book":
                tmp[2] = float(tmp[2])
                books += tmp[2]
            elif tmp[1] == "DVD":
                tmp[2] = float(tmp[2])
                dvds += tmp[2]
            elif tmp[1] == "Game":
                tmp[2] = float(tmp[2])
                games += tmp[2]
        except ValueError:
            print(f'Error on line {line_counter}: Could not convert "{tmp[2]}" to price format')
        finally:
            line_counter += 1

    file1.close()

    # Since the logic of writing the output to a new file is inside the
    # 'with' context manager, it is not necessary to call the 'close' method
    with open("daily_report.txt", 'a') as file2:
        file2.write(f"Books: ${books:.2f}\n")
        file2.write(f"DVDs: ${dvds:.2f}\n")
        file2.write(f"Games: ${games:.2f}\n")


main()
