#
# Alex Cesar Rosa
# 6/11/2024
#

def main():
    user_input = get_input()
    print(f"All scores: {user_input}")
    print("Students who scored below 60 get 10 extra points.")

    final_scores = manage_scores(user_input)
    print(f"All scores: {final_scores}")

    print("Students whose scores have changed:")
    score_analysis(user_input, final_scores)


def get_input():
    user_input = list()
    for i in range(5):
        user_input.append(float(input("Enter a test score: ")))
    return user_input


def manage_scores(scores):
    final_scores = list()
    for i in scores:
        if i < 60:
            i += 10
            final_scores.append(i)
        else:
            final_scores.append(i)
    return final_scores


def score_analysis(initial_score, final_score):
    for i in range(5):
        if initial_score[i] != final_score[i]:
            print(f"Old score: {initial_score[i]} New score: {final_score[i]}")
        else:
            continue


if __name__ == '__main__':
    main()