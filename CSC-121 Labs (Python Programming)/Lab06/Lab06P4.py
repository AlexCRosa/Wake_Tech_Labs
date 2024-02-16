#
# Alex Cesar Rosa
# 2/16/2024
# This program helps a user generate a line graph
#

import matplotlib.pyplot as plt

plt.title(input(f"Enter the bar graph title: "))
plt.xlabel(input("Enter the label for the x-axis: "))
plt.ylabel(input("Enter the label for the y-axis: "))

data_amount = int(input("Enter the number of data points: "))

x_axis = []
y_axis = []
for i in range(1, data_amount + 1):
    tick_x = input(f"Enter the name for tick {i}: ")
    x_axis.append(tick_x)
    tick_y = float(input(f"Enter the value for tick {i}: "))
    y_axis.append(tick_y)

plt.bar(x_axis, y_axis)
plt.show()