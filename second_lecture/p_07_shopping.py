budget = float(input())
video_n = int(input())
proc_n = int(input())
ram_n = int(input())

video_price = video_n * 250
proc_price = proc_n * (video_price * 0.35)
ram_price = ram_n * (video_price * 0.1)

total_cost = video_price + proc_price + ram_price

if video_n > proc_n:
    total_cost = total_cost * 0.85

diff = abs(budget - total_cost)

if budget >= total_cost:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")