name_team = input()
n_games = int(input())

total_points = 0
W = 0
D = 0
L = 0

zero_flag = False

for _ in range(n_games):
    result = input()
    if result == "W":
        total_points += 3
        W += 1
    elif result == "D":
        total_points += 1
        D += 1
    elif result == "L":
        L += 1
    else:
        n_games = 0
        zero_flag = True

if n_games == 0:
    zero_flag = True
    print(f"{name_team} hasn't played any games during this season.")

else:
    won_games_percent = W / n_games * 100
    print(f"{name_team} has won {total_points} points during this season.")
    print("Total stats:")
    print(f"## W: {W}")
    print(f"## D: {D}")
    print(f"## L: {L}")
    print(f"Win rate: {won_games_percent:.2f}%")




