budget = float(input())
product_name = input()
count_product = 0
total_cost = 0
remaining_money = 0
flag = False

while budget > 0:
    if product_name == "Stop":
        flag = True
        break
    product_cost = float(input())
    count_product += 1

    if count_product % 3 == 0:
        product_cost *= 0.5
    total_cost += product_cost
    budget -= total_cost

    product_name = input()

budget_abs = abs(budget)

if flag:
    print(f"You bought {count_product} products for {total_cost:.2f} leva.")
else:
    print("You don't have enough money!")
    print(f"You need {budget_abs:.2f} leva!")







