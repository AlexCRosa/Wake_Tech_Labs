#
# Alex Rosa
# 1/10/2024
# This program calculates the time it takes to travel
# a certain distance going a specific speed.
#
# Note: The miles and speed entered could be a floating point
# number.
#

# Get the number of miles.
miles = float(input("Enter a number of miles: "))

# Get the speed in MPH.
speed = float(input("Enter speed in MPH: "))

# Calculate the travel time.
travel_time = miles / speed

# Display the travel time (formatted to 2 decimal places).
print(f"You should cover that distance in {travel_time:.2f} hours.")
