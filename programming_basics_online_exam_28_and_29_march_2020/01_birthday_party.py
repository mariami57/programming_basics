hall_rent = float(input())

cake_price = hall_rent * 0.2
drinks_price = cake_price * 0.55
animator_price = hall_rent / 3

total_cost = hall_rent + cake_price + drinks_price + animator_price

print(total_cost)