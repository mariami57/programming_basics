import sys
n_easter_breads = int(input())

max_points = - sys.maxsize
max_baker = ""

for baker in range(n_easter_breads):
    baker_name = input()
    input_line = input()

    current_baker_points = 0

    while input_line != "Stop":
        points = int(input_line)
        current_baker_points += points

        input_line = input()

    print(f"{baker_name} has {current_baker_points} points.")

    if current_baker_points > max_points:
        max_points = current_baker_points
        max_baker = baker_name
        print(f"{max_baker} is the new number 1!")

print(f"{max_baker} won competition with {max_points} points!")
