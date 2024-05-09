price_trip = float(input())
puzzle_n = int(input())
dolls_n = int(input())
bears_n = int(input())
minions_n = int(input())
trucks_n = int(input())

total_number_of_toys = puzzle_n + dolls_n + bears_n + minions_n + trucks_n

revenue = (puzzle_n * 2.6) + (dolls_n * 3) + (bears_n * 4.1) + (minions_n * 8.2) + (trucks_n * 2)


total_number_of_toys = puzzle_n + dolls_n + bears_n + minions_n + trucks_n

if total_number_of_toys >= 50:
    revenue = revenue - (revenue * 0.25)

revenue = revenue - (revenue * 0.1 )

difference = price_trip - revenue_after_discount_and_rent
difference = abs(difference)

if price_trip <= revenue_after_discount_and_rent:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference} lv needed.")