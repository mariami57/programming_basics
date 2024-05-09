budget = float(input())
extras_n = int(input())
clothing_price = float(input())

total_cost_clothing = extras_n * clothing_price
decor_price = budget * 0.1

if extras_n > 150:
    total_cost_clothing = total_cost_clothing * 0.9

total_cost_all = total_cost_clothing + decor_price

diff = abs(budget - total_cost_all)

if budget >= total_cost_all:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")

else:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
