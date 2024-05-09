n_games_sold = int(input())
hearthstone = 0
fornite = 0
overwatch = 0
others = 0


for _ in range(n_games_sold):
    current_game = input()
    if current_game == "Hearthstone":
        hearthstone += 1
    elif current_game == "Fornite":
        fornite += 1
    elif current_game == "Overwatch":
        overwatch += 1
    else:
        others += 1

hearthstone_percent = hearthstone / n_games_sold * 100
fornite_percent = fornite / n_games_sold * 100
overwatch_percent = overwatch / n_games_sold * 100
others_percent = others / n_games_sold * 100


print(f"Hearthstone - {hearthstone_percent:.2f}%")
print(f"Fornite - {fornite_percent:.2f}%")
print(f"Overwatch - {overwatch_percent:.2f}%")
print(f"Others - {others_percent:.2f}%")
