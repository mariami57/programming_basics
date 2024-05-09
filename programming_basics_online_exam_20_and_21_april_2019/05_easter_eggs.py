import sys

eggs_n = int(input())

red, orange, blue, green = 0, 0, 0, 0

max_number = - sys.maxsize
max_colour = ""

for _ in range(eggs_n):
    colour = input()
    if colour == "red":
        red += 1
    elif colour == "orange":
        orange += 1
    elif colour == "blue":
        blue += 1
    elif colour == "green":
        green += 1

    if red > max_number:
        max_number = red
        max_colour = "red"
    elif orange > max_number:
        max_number = orange
        max_colour = "orange"
    elif blue > max_number:
        max_number = blue
        max_colour = "blue"
    elif green > max_number:
        max_number = green
        max_colour = "green"

print(f"Red eggs: {red}")
print(f"Orange eggs: {orange}")
print(f"Blue eggs: {blue}")
print(f"Green eggs: {green}")
print(f"Max eggs: {max_number} -> {max_colour}")


