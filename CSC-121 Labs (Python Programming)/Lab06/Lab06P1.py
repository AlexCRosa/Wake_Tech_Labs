#
# Alex Cesar Rosa
# 2/12/2024
# This program manages the scores of three students
#
all_scores = []
a_list = all_scores
b_list = all_scores
c_list = all_scores

students = ["Ashley", "Barb", "Carl"]

for student in students:
    if student == "Ashley":
        amount_scores = 3
        print(f"Please enter {student}'s scores one by one.")

        for test in range(amount_scores):
            score = int(input("Enter a score: "))
            all_scores.append(score)

        print(f"Ashley's scores: {all_scores[:3]}")
        print()

    elif student == "Barb":
        amount_scores = 5
        print(f"Please enter {student}'s scores one by one.")

        for test in range(amount_scores):
            score = int(input("Enter a score: "))
            all_scores.append(score)

        print(f"Barb's scores: {all_scores[3:8]}")
        print()

    elif student == "Carl":
        amount_scores = 4
        print(f"Please enter {student}'s scores one by one.")

        for test in range(amount_scores):
            score = int(input("Enter a score: "))
            all_scores.append(score)

        print(f"Carl's scores: {all_scores[8:12]}")
        print()

all_scores = [a_list[:3], b_list[3:8], c_list[8:12]]
print(f"All scores: {all_scores}")

# Populating the spreads' list with temporary sum of values
score_spreads = []

for temp_element in range(3):
    temp = sum(all_scores[temp_element])
    score_spreads.append(temp)

# Giving the extra credit and converting back to integer

for outer_element in range(3):
    for inner_element in range(len(all_scores[outer_element])):
        all_scores[outer_element][inner_element] = all_scores[outer_element][inner_element] * 1.05

for outer_element in range(3):
    for inner_element in range(len(all_scores[outer_element])):
        all_scores[outer_element][inner_element] = int(all_scores[outer_element][inner_element])

print(f"All scores after extra credit: {all_scores}")

# Processing the spread list
temp_list = []
for i in range(3):
    temp = sum(all_scores[i])
    temp_list.append(temp)

    score_spreads[i] -= (temp_list[i])
    score_spreads[i] = -(score_spreads[i])

print(f"Score spreads: {score_spreads}")
print()

print("Original Scores")
print(f"Ashley's scores: {a_list[:3]}")
print(f"Barb's scores: {b_list[3:8]}")
print(f"Carl's scores: {c_list[8:12]}")
