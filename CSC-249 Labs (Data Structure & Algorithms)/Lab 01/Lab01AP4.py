#
# Alex Cesar Rosa
# 5/28/2024
#

scoreA = 0
scoreB = 0

for i in range(4):
    print(f"Quarter {i + 1}")

    # Team A
    scoreA += int(input("Enter team A score: "))
    print(f"Team A total score so far: {scoreA}")

    # Team B
    scoreB += int(input("Enter team B score: "))
    print(f"Team B total score so far: {scoreB}")

if scoreA == scoreB:
    print("The game is tied. Let's play overtime")

    for i in range(2):
        print(f"Overtime {i + 1}")

        # Team A
        scoreA += int(input("Enter team A score: "))
        print(f"Team A total score so far: {scoreA}")

        # Team B
        scoreB += int(input("Enter team B score: "))
        print(f"Team B total score so far: {scoreB}")

if scoreA > scoreB:
    print("Team A has won")
else:
    print("Team B has won")

