fruit = input()
size = input()
set_number = int(input())
price = 0

if size == "small":
    if fruit == "Watermelon":
        price = 2 * 56
    elif fruit == "Mango":
        price = 2 * 36.66
    elif fruit == "Pineapple":
        price = 2 * 42.10
    elif fruit == "Raspberry":
        price = 2 * 20
elif size == "big":
    if fruit == "Watermelon":
        price = 5 * 28.70
    elif fruit == "Mango":
        price = 5 * 19.60
    elif fruit == "Pineapple":
        price = 5 * 24.80
    elif fruit == "Raspberry":
        price = 5 * 15.20

total_price = price * set_number
if 400 <= total_price <= 1000:
    total_price *= 0.85
elif total_price > 1000:
    total_price *= 0.50

print(f"{total_price:.2f} lv.")