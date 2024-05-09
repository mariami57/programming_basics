strawberry_price = float(input())
bananas = float(input())
oranges = float(input())
raspberries = float(input())
strawberries = float(input())

raspberry_price = strawberry_price * 0.5
orange_price = raspberry_price * 0.6
banana_price = raspberry_price * 0.2

total_cost = (strawberries * strawberry_price) + (bananas * banana_price) + (orange_price * oranges) + (raspberry_price * raspberries)

print(f"{total_cost:.2f}")