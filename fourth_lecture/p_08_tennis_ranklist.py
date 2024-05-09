import math

tournaments_n = int(input())
initial_points = int(input())


points_from_tournaments = 0
wins = 0

for _ in range(tournaments_n):
    i = input()
    if i == "W":
        points_from_tournaments += 2000
        wins += 1
    elif i == "F":
        points_from_tournaments += 1200
    elif i == "SF":
        points_from_tournaments += 720


total_points = initial_points + points_from_tournaments
average_points = math.floor(points_from_tournaments / tournaments_n)
tournaments_won_percentage = wins / tournaments_n * 100

print(f"Final points: {total_points}")
print(f"Average points: {average_points}")
print(f"{tournaments_won_percentage:.2f}%")
