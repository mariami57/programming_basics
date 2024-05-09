budget = float(input())
series_n = int(input())

total_price = 0

for _ in range(series_n):
    series_name = input()
    current_price = float(input())
    if series_name == "Thrones":
        current_price = current_price * 0.5
    elif series_name == "Lucifer":
        current_price = current_price * 0.6
    elif series_name == "Protector":
        current_price = current_price * 0.7
    elif series_name == "TotalDrama":
        current_price = current_price * 0.8
    elif series_name == "Area":
        current_price = current_price * 0.9

    total_price += current_price

diff = abs(total_price - budget)

if total_price <= budget:
    print(f"You bought all the series and left with {diff:.2f} lv.")
else:
    print(f"You need {diff:.2f} lv. more to buy the series!")





