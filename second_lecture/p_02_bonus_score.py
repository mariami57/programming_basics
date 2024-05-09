grade = int(input())

bonus_points = 0

if grade <= 100:
    bonus_points = 5

elif 100 < grade <= 1000:
    bonus_points = grade * 0.2

elif grade > 1000:
    bonus_points = grade * 0.1


if grade % 2 == 0:
    bonus_points = bonus_points + 1

if grade % 10 == 5:
    bonus_points = bonus_points + 2

total_points = grade + bonus_points

print(bonus_points)
print(total_points)
