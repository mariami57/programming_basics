budget = float(input())
fuel_litres = float(input())
day = input()

fuel_cost = fuel_litres * 2.1
total_costs = fuel_cost + 100

if day == "Saturday":
    total_costs = total_costs * 0.9

elif day == "Sunday":
    total_costs = total_costs * 0.8

diff = abs(total_costs - budget)

if total_costs <= budget:
    print(f"Safari time! Money left: {diff:.2f} lv. ")

else:
    print(f"Not enough money! Money needed: {diff:.2f} lv.")
