#
# Alex Cesar Rosa
# 2/14/2024
# This program tests the student understanding of tuples
#
import random

# Step A
print("Step a:")
amount_values = int(input("How many values to put in the tuple? "))

# Step B
print("Step b:")
start_value = int(input("What is the start of the range? "))
end_value = int(input("What is the end of the range? "))

# Step C
# It is called Tuple. However, I defined it as a list to accept appending values
temporary_list = []

for element in range(amount_values):
    temporary_list.append(random.randint(start_value, end_value))

print(f"Step c: Tuple of 8 random numbers: {tuple(temporary_list)}")

# Step D
print(f"Step d: Tuple of first 4 numbers: {tuple(temporary_list[:4])}")

# Step E
print(f"Step e: Tuple of last 2 numbers: {tuple(temporary_list[-2:])}")

# Step F
print(f"Step f: Two tuples concatenated: {tuple(temporary_list[-2:]) + tuple(temporary_list[:4])}")

# Step G
for element in range(len(temporary_list)):
    temporary_list[element] += 1

print(f"Step g: Two tuples concatenated and incremented: {tuple(temporary_list[-2:]) + tuple(temporary_list[:4])}")