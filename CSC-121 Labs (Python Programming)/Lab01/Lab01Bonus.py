#
# Alex Rosa
# 1/10/2024
# This program calculates the time it takes to travel
# a certain distance going a specific speed.
#
# Note: The miles and speed entered could be a floating point
# number.
#

# Input
miles = float(input("Enter a number of miles: "))
speed = float(input("Enter speed in MPH: "))

# Processing
travel_time = (miles / speed) * 60  # Total amount of minutes
hours_remaining = int(travel_time // 60)
minutes_remaining = travel_time % 60

# Output
print(f"You should cover that distance in {hours_remaining} hours and {minutes_remaining:.2f}.")