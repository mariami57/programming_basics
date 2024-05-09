movie = input()
hall_type = input()
tickets_n = int(input())

price_ticket = 0
if hall_type == "normal":
    if movie == "A Star Is Born":
        price_ticket = 7.5
    elif movie == "Bohemian Rhapsody":
        price_ticket = 7.35
    elif movie == "Green Book":
        price_ticket = 8.15
    elif movie == "The Favourite":
        price_ticket = 8.75

elif hall_type == "luxury":
    if movie == "A Star Is Born":
        price_ticket = 10.5
    elif movie == "Bohemian Rhapsody":
        price_ticket = 9.45
    elif movie == "Green Book":
        price_ticket = 10.25
    elif movie == "The Favourite":
        price_ticket = 11.55

elif hall_type == "ultra luxury":
    if movie == "A Star Is Born":
        price_ticket = 13.5
    elif movie == "Bohemian Rhapsody":
        price_ticket = 12.75
    elif movie == "Green Book":
        price_ticket = 13.25
    elif movie == "The Favourite":
        price_ticket = 13.95

revenue = price_ticket * tickets_n

print(f"{movie} -> {revenue:.2f} lv.")
