# От конзолата се четат 4 реда:
# Бюджет на филма – реално число в диапазона [100 000.0… 2 000 000.0]
# Дестинация – текст, с възможности "Dubai", "Sofia" и "London"
# Сезон – текст, с възможности "Summer" и "Winter"
# Брой дни  – цяло число в диапазона [1… 40]

budget = float(input())
destination = input()
season = input()
days_n = int(input())

cost = 0

if season == "Summer":
    if destination == "Dubai":
        cost = 40000 * days_n * 0.7
    elif destination == "Sofia":
        cost = 12500 * days_n * 1.25
    elif destination == "London":
        cost = 20250 * days_n
elif season == "Winter":
    if destination == "Dubai":
        cost = 45000 * days_n * 0.7
    elif destination == "Sofia":
        cost = 17000 * days_n * 1.25
    elif destination == "London":
        cost = 24000 * days_n

diff = abs(budget - cost)
if budget >= cost:
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")
else:
    print(f"The director needs {diff:.2f} leva more!")

