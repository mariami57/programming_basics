food = int(input())
input_line = input()
food_in_gr = food * 1000
total_food_eaten = 0
while input_line != "Adopted":
    meal_gr = int(input_line)
    total_food_eaten += meal_gr

    input_line = input()

diff = abs(food_in_gr - total_food_eaten)

if food_in_gr >= total_food_eaten:
    print(f"Food is enough! Leftovers: {diff} grams.")
else:
    print(f"Food is not enough. You need {diff} grams more." )
