movie = input()
package = input()
tickets_n = int(input())

price = 0

if movie == "John Wick":
    if package == "Drink":
        price = 12
    elif package == "Popcorn":
        price = 15
    elif package == "Menu":
        price = 19
elif movie == "Star Wars":
    if package == "Drink":
        price = 18
    elif package == "Popcorn":
        price = 25
    elif package == "Menu":
        price = 30
elif movie == "Jumanji":
    if package == "Drink":
        price = 9
    elif package == "Popcorn":
        price = 11
    elif package == "Menu":
        price = 14

if movie == "Jumanji" and tickets_n == 2:
    total_cost = price * tickets_n * 0.85
elif movie == "Star Wars" and tickets_n >= 4:
    total_cost = price * tickets_n * 0.7
else:
    total_cost = price * tickets_n

print(f"Your bill is {total_cost:.2f} leva.")