#
# Alex Cesar Rosa
# 6/4/2024
#

with open("payroll_data.txt", "r") as payroll:

    # Print Header
    print("Name", end=" " * (10 - len("Name")))
    print("Rate".rjust(12, " "), end=" ")
    print("Hours".rjust(15, " "), end=" ")
    print("Total Pay".rjust(15, " "))

    # Iterate through the lines of the file
    for line in payroll:
        # Create a list with the line content
        employee_info = line.split()

        # Add Total Pay to the line list
        employee_info.append(str(f"{float(employee_info[1]) * float(employee_info[2]):.2f}"))

        # Iterate through the elements of the line list
        for i in employee_info:
            # Check if the string element is made of numbers
            if i.replace(".", "1").isdigit():

                # Add a second decimal to numerical strings that have only one decimal
                if len(i) < 5:
                    i += "0"

                print(i.rjust(15, " "), end= " ")
            else:
                print(i, end=" " * (7 - len(i)))

        # Go to the next line after iterating through all the elements of the line
        print()
