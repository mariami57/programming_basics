import math

height = int(input())
width = int(input())
area_remaining_percentage = int(input())
input_line = input()
paint_left = False
no_paint_no_walls = False
walls_total_area = height * width * 4
area_remaining = walls_total_area * area_remaining_percentage / 100
walls_for_painting = math.ceil(walls_total_area - area_remaining)

while input_line != "Tired!":
    current_litres = int(input_line)
    walls_for_painting -= current_litres

    if walls_for_painting < 0:
        paint_left = True
        break
    elif walls_for_painting == 0:
        no_paint_no_walls = True
        break
    input_line = input()
walls_for_painting_abs = abs(walls_for_painting)

if input_line == "Tired!":
    print(f"{walls_for_painting} quadratic m left.")

if paint_left:
    print(f"All walls are painted and you have {walls_for_painting_abs} l paint left!")
elif no_paint_no_walls:
    print("All walls are painted! Great job, Pesho!" )










