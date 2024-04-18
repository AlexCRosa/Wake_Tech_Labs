#
# Alex Cesar Rosa
# 4/21/2024
# ITS Python Certification Review - Problem 1 (Datetime module)
#

from datetime import datetime, date, time


def main():
    current_datetime = datetime.now()

    print("The current date/time is:")
    print(current_datetime.strftime('%m/%d/%y %H:%M:%S %p'))
    print(current_datetime.strftime('%A, %b %d, %Y'))
    print(current_datetime.strftime('%a, %B %d, %Y'))

    user_datetime = input("Enter a date (e.g. mm/dd/yyyy): ")
    user_datetime = datetime.strptime(user_datetime, "%m/%d/%Y")
    print(f"That date was on a {user_datetime.strftime('%A')}.")


main()
