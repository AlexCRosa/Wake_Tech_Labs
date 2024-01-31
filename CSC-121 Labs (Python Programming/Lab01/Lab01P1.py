#
# Alex Rosa
# 1/10/2024
# This is the problem 01 for the first lab of CSC-121
#

import datetime

name = input('What is your name? ')
print(f'Welcome to CSC121 {name}!')
print(f'Today is {datetime.date.today():%B %d, %Y}')
print('I hope you learn a lot of Python this semester!')