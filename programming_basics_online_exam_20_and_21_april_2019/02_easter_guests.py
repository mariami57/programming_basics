import math

guests_n = int(input())
budget = int(input())

easter_bread_n = math.ceil(guests_n / 3)
eggs_n = guests_n * 2

easter_bread_price = easter_bread_n * 4
eggs_price = eggs_n * 0.45

total_cost = easter_bread_price + eggs_price

diff = abs(total_cost - budget)

if budget >= total_cost:
    print(f"Lyubo bought {easter_bread_n} Easter bread and {eggs_n} eggs.")
    print(f"He has {diff:.2f} lv. left.")

else:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {diff:.2f} lv. more.")