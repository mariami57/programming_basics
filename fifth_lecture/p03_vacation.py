target = float(input())
money = float(input())
spend_counter = 0
days_counter = 0
spender_flag = False

while money < target:
    days_counter += 1
    action = input()
    current_money = float(input())

    if action == "spend":
        money -= current_money
        spend_counter += 1
        if spend_counter == 5:
            spender_flag = True
            break

    elif action == "save":
        money += current_money
        spend_counter = 0

    if money < 0:
        money = 0

if spender_flag:
    print("You can't save the money.")
    print(f"{days_counter}")
else:
    print(f"You saved the money for {days_counter} days.")


