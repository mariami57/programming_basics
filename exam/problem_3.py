people_n = int(input())
season = input()
price = 0
if people_n <= 5:
    if season == "spring":
        price = 50
    elif season == "summer":
        price = 48.5
    elif season == "autumn":
        price = 60
    elif season == "winter":
        price = 86
elif people_n > 5:
    if season == "spring":
        price = 48
    elif season == "summer":
        price = 45
    elif season == "autumn":
        price = 49.5
    elif season == "winter":
        price = 85

total_cost = price * people_n
if season == "summer":
    total_cost *= 0.85
elif season == "winter":
    total_cost *= 1.08

print(f"{total_cost:.2f} leva.")