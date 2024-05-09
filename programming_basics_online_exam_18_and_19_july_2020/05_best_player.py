import sys

name = input()
max_goals = -sys.maxsize
best_player = " "
hat_trick_scorer = ""

while name != "END":
    goals_n = int(input())

    if goals_n >= 3:
        hat_trick_scorer = name
    if goals_n > max_goals:
        max_goals = goals_n
        best_player = name
    if goals_n >= 10:
        break
    name = input()

print(f"{best_player} is the best player!")

if max_goals >= 3:
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max_goals} goals.")

