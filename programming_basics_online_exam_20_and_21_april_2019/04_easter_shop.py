init_quantity = int(input())
input_line = input()
flag = False
eggs_sold =0
while input_line != "Close":
    n_eggs = int(input())

    if input_line == "Buy" and init_quantity < n_eggs:
        flag = True
        break
    if input_line == "Buy":
        init_quantity -= n_eggs
        eggs_sold += n_eggs
    elif input_line == "Fill":
        init_quantity += n_eggs

    input_line = input()

if flag:
    print("Not enough eggs in store!")
    print(f"You can buy only {init_quantity}.")
else:
    print("Store is closed!")
    print(f"{eggs_sold} eggs sold.")

