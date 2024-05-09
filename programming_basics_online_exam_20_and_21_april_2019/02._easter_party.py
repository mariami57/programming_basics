guests_n = int(input())
meal_price = float(input())
budget = float(input())


if 10 <= guests_n <= 15:
    meal_price = meal_price * 0.85

elif 15 < guests_n <= 20:
    meal_price = meal_price * 0.80

elif guests_n > 20:
    meal_price = meal_price * 0.75

meal_total_cost = meal_price * guests_n

cake_price = budget * 0.1

total_costs = meal_total_cost + cake_price

diff = abs(total_costs - budget)

if budget >= total_costs:
    print(f"It is party time! {diff:.2f} leva left.")

else:
    print(f"No party! {diff:.2f} leva needed.")
