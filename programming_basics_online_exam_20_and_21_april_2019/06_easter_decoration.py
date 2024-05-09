clients_num = int(input())
price = 0
cost_all_clients = 0
for client in range(clients_num):
    purchase = input()
    purchase_num = 0
    total_cost = 0
    while purchase != "Finish":
        purchase_num += 1
        if purchase == "basket":
            price = 1.5
        elif purchase == "wreath":
            price = 3.8
        elif purchase == "chocolate bunny":
            price = 7

        total_cost += price
        purchase = input()
    if purchase_num % 2 == 0:
        total_cost *= 0.8
    if purchase == "Finish":
        print(f"You purchased {purchase_num} items for {total_cost:.2f} leva.")
        cost_all_clients += total_cost


avg_bill = cost_all_clients / clients_num
print(f"Average bill per client is: {avg_bill:.2f} leva.")


