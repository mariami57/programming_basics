price_veg_per_kg = float(input())
price_fruit_per_kg = float(input())
total_kg_veg = int(input())
total_kg_fruit = int(input())

veg_total_rpice = price_veg_per_kg * total_kg_veg
fruit_total_price = price_fruit_per_kg * total_kg_fruit

total_sum = veg_total_rpice + fruit_total_price
total_sum_eur = total_sum / 1.94

print(f"{total_sum_eur:.2f}")