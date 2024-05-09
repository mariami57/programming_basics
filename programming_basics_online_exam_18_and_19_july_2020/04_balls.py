import math

n_balls = int(input())
red, orange, yellow, white, black, other = 0, 0, 0, 0, 0, 0

points = 0

for _ in range(n_balls):
    colour = input()
    if colour == "red":
        points += 5
        red += 1
    elif colour == "orange":
        points += 10
        orange += 1
    elif colour == "yellow":
        points += 15
        yellow += 1
    elif colour == "white":
        points += 20
        white += 1
    elif colour == "black":
        points = math.floor(points / 2)
        black += 1
    else:
        other += 1
        continue

print(f"Total points: {points}")
print(f"Red balls: {red}")
print(f"Orange balls: {orange}")
print(f"Yellow balls: {yellow}")
print(f"White balls: {white}")
print(f"Other colors picked: {other}")
print(f"Divides from black balls: {black}")
