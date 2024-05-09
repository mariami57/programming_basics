walk_minutes = int(input())
walk_n = int(input())
cat_calories_intake = int(input())

total_time_walks = walk_n * walk_minutes
total_calories_burnt = total_time_walks * 5
half_calories_intake = cat_calories_intake * 0.5

diff = abs(total_calories_burnt - half_calories_intake)

if half_calories_intake <= total_calories_burnt:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {total_calories_burnt}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {total_calories_burnt}.")
