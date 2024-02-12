#
# Alex Cesar Rosa
# 2/5/2024
# This program calculates the total cost for items purchased at Bargain
#
taken_test = [3, 5, 4]

all_scores = []

for student in ["Ashley", "Barb", "Carl"]:
    print(f"Please enter {student}'s scores one by one.")

    for amount in taken_test:
        tests = 0

        while tests < amount:
            for element in [0, 1, 2]:
                score = int(input("Enter a score: "))
                all_scores[element].append(score)