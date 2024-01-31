#
# Student Name
# Date
# Pretty Pattern Generator
#
# NOTE: With the range functions, you may use 
# one, two, or three parameters to accomplish 
# your task.
FillThisIn = None  # Replace FillThisIn with correct code below

# Ask the user for the number of rows
num_rows = int(input("How many rows? "))
# Ask the user for the number of columns
num_columns = int(input("How many columns? "))

# Iterate over the rows.
for row in range(num_rows):

    if row % 2 == 1:
        # Iterate over the columns.
        for col in range(num_columns):
            # Test if the row and column are even numbered
            if col % 2 != 0 and col <= num_columns:
                print(' ', end='')
            else:
                print('*', end='')
    elif row % 2 == 0:
        # Iterate over the columns.
        for col in range(num_columns):
            print('*', end='')

    # Go to the next row.
    print()
