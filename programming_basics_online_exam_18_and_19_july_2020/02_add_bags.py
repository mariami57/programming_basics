price_above_20_kg = float(input())
luggage_kg = float(input())
days_trip = int(input())
luggage_n = int(input())

luggage_price = 0

if luggage_kg < 10:
    luggage_price = price_above_20_kg * 0.2

elif 10 <= luggage_kg <= 20:
    luggage_price = price_above_20_kg * 0.5

else:
    luggage_price = price_above_20_kg


if days_trip > 30:
    luggage_price = luggage_price * 1.1

elif 7 <= days_trip <= 30:
    luggage_price = luggage_price * 1.15

else:
    luggage_price = luggage_price * 1.4

total_sum = luggage_price * luggage_n

print(f"The total price of bags is: {total_sum:.2f} lv. ")