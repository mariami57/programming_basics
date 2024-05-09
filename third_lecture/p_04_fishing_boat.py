budget = int(input())
season = input()
fishermen_n = int(input())

boat_price = 0

if season == "Spring":
    boat_price = 3000
elif season == "Summer" or season == "Autumn":
    boat_price = 4200
elif season == "Winter":
    boat_price = 2600

if fishermen_n <= 6:
    boat_price = boat_price * 0.9

elif 7 <= fishermen_n <= 11:
    boat_price = boat_price * 0.85

elif fishermen_n >= 12:
    boat_price = boat_price * 0.75

if fishermen_n % 2 == 0 and (season == "Spring" or season == "Summer" or season == "Winter"):
    boat_price = boat_price * 0.95

diff = abs(boat_price - budget)

if boat_price <= budget:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")

