size = input()
colour = input()
batch_n = int(input())
price = 0

if colour == "Red":
    if size == "Large":
        price = 16
    elif size == "Medium":
        price = 13
    elif size == "Small":
        price = 9
elif colour == "Green":
    if size == "Large":
        price = 12
    elif size == "Medium":
        price = 9
    elif size == "Small":
        price = 8
elif colour == "Yellow":
    if size == "Large":
        price = 9
    elif size == "Medium":
        price = 7
    elif size == "Small":
        price = 5

total_revenue = batch_n * price
profit = total_revenue - (total_revenue * 0.35)

print(f"{profit:.2f} leva.")
