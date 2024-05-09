destination = input()
dates = input()
n_stays = int(input())
price = 0

if dates == "21-23":
    if destination == "France":
        price = 30
    elif destination == "Italy":
        price = 28
    elif destination == "Germany":
        price = 32
elif dates == "24-27":
    if destination == "France":
        price = 35
    elif destination == "Italy":
        price = 32
    elif destination == "Germany":
        price = 37
elif dates == "28-31":
    if destination == "France":
        price = 40
    elif destination == "Italy":
        price = 39
    elif destination == "Germany":
        price = 43

total_cost = price * n_stays

print(f"Easter trip to {destination} : {total_cost:.2f} leva.")
