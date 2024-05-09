player_name = input()
hat_trick = False
best_player = ""
best_goals = 0
while player_name != "END":
    current_goals = int(input())
    if current_goals >= 3:
        hat_trick = True

    if current_goals > best_goals:
        best_goals = current_goals
        best_player = player_name
    if current_goals >= 10:
        break
    player_name = input()

print(f"{best_player} is the best player!")

if hat_trick:
    print(f"He has scored {best_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {best_goals} goals.")
