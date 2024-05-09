n_days = int(input())
total_food = float(input())
dog_eaten = 0
cat_eaten = 0
biscuits = 0
for days_counter in range(1, n_days+1):
    dog_food = int(input())
    cat_food = int(input())
    dog_eaten += dog_food
    cat_eaten += cat_food

    if days_counter % 3 == 0:
        biscuits += (dog_food + cat_food) * 0.10

total_food_eaten = cat_eaten + dog_eaten
biscuits_rounded = round(biscuits)

total_food_eaten_percentage = total_food_eaten / total_food * 100
dog_eaten_percentage = dog_eaten / total_food_eaten * 100
cat_eaten_percentage = cat_eaten / total_food_eaten * 100

print(f"Total eaten biscuits: {biscuits_rounded}gr.")
print(f"{total_food_eaten_percentage:.2f}% of the food has been eaten.")
print(f"{dog_eaten_percentage:.2f}% eaten from the dog.")
print(f"{cat_eaten_percentage:.2f}% eaten from the cat.")
