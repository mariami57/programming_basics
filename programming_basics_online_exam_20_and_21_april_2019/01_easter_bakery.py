flour_price = float(input())
flour_kg = float(input())
sugar_kg = float(input())
carton_eggs_n = int(input())
yeast_n = int(input())

sugar_price = flour_price * 0.75
carton_eggs_price = flour_price * 1.1
yeast_price = sugar_price * 0.2

flour_cost = flour_kg * flour_price
sugar_cost = sugar_kg * sugar_price
carton_eggs_cost = carton_eggs_n * carton_eggs_price
yeast_cost = yeast_price * yeast_n

total_cost = flour_cost + sugar_cost + carton_eggs_cost + yeast_cost

print(f"{total_cost:.2f}")
