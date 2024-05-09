first_player = input()
second_player = input()
input_line = input()

first_points = 0
second_points = 0
first_points_sum = 0
second_points_sum = 0
winner = ""
winner_points = 0
flag = False
while input_line != "End of game":
    first_player_card = int(input_line)
    second_player_card = int(input())

    if first_player_card > second_player_card:
        first_points = first_player_card - second_player_card
        first_points_sum += first_points
        flag = False
    elif first_player_card < second_player_card:
        second_points = second_player_card - first_player_card
        second_points_sum += second_points
        flag = False
    else:
        flag = True
        first_player_card = int(input())
        second_player_card = int(input())
        if first_player_card > second_player_card:
            winner = first_player
            winner_points = first_points_sum
        elif first_player_card < second_player_card:
            winner = second_player
            winner_points = second_points_sum
        break

    input_line = input()


if flag:
    print("Number wars!")
    print(f"{winner} is winner with {winner_points} points")
else:
    print(f"{first_player} has {first_points_sum} points")
    print(f"{second_player} has {second_points_sum} points")
