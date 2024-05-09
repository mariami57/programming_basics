name = input()
best_player = ""
best_points = 0
while name != "Stop":
    points = 0
    for letter in name:
        current_number = int(input())
        if current_number == ord(letter):
            points += 10
        else:
            points += 2

        if points >= best_points:
            best_points = points
            best_player = name
    name = input()

print(f"The winner is {best_player} with {best_points} points!")