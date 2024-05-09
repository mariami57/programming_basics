import math

n_days = int(input())
food_kg = int(input())
first_deer_food = float(input())
second_deer_food = float(input())
third_deer_food = float(input())

first_deer_needed = first_deer_food * n_days
second_deer_needed = second_deer_food * n_days
third_deer_needed = third_deer_food * n_days
total_food_needed = first_deer_needed + second_deer_needed + third_deer_needed

diff = abs(food_kg - total_food_needed)


if total_food_needed <= food_kg:
    diff_floor = math.floor(diff)
    print(f"{diff_floor} kilos of food left.")
else:
    diff_ceil = math.ceil(diff)
    print(f"{diff_ceil} more kilos of food are needed.")