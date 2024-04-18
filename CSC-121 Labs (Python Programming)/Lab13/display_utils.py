#
# WT Instructors
# 3/16/2023
# This module will display various messages as indicated
# in the function comment headers.
#

# This function will return a greeting for the user
# whose name is passed in to the function.
def get_user_greeting(name):
    # This line has a bug which should be caught
    # by the automated testing!
    return f'Hello-{name}!'


# This function will return True if the first two
# parameters added together are greater than the third
# parameter.
def sum_is_greater(first, second, third):
    if first + second > third:
        return True
    else:
        return False
