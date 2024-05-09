days_stay = int(input())
place = input()
review = input()

nights_stay = days_stay - 1
total_cost = 0

if place == "room for one person":
    total_cost = nights_stay * 18

elif place == "apartment":
    if days_stay < 10:
        total_cost = (nights_stay * 25) * 0.7
    elif 10 <= days_stay < 15:
        total_cost = (nights_stay * 25) * 0.65
    else:
        total_cost = (nights_stay * 25) * 0.5

elif place == "president apartment":
    if days_stay < 10:
        total_cost = (nights_stay * 35) * 0.9
    elif 10 <= days_stay < 15:
        total_cost = (nights_stay * 35) * 0.85
    else:
        total_cost = (nights_stay * 35) * 0.8


if review == "positive":
    total_cost = (total_cost * 0.25) + total_cost
elif review == "negative":
    total_cost = total_cost * 0.9

print (f"{total_cost:.2f}")

