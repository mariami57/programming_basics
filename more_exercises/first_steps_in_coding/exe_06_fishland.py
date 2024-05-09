sku_price = float(input())
caca_price = float(input())
pal_kg = float(input())
saf_kg = float(input())
oyster_kg = int(input())

pal_price_per_unit = sku_price + (sku_price * 0.6)
pal_total_cost = pal_price_per_unit * pal_kg

saf_price = caca_price + (caca_price * 0.8)
saf_total_cost = saf_price * saf_kg

oyster_total_cost = oyster_kg * 7.5

total_cost_all = pal_total_cost + saf_total_cost + oyster_total_cost

print(f"{total_cost_all:.2f}")