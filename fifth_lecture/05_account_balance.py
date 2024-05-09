total_sum = 0


while True:
    current_deposit = input()

    if current_deposit == "NoMoreMoney":
        break

    current_sum = float(current_deposit)

    if current_sum >= 0:
        total_sum += current_sum
        print(f"Increase: {current_sum:.2f}")

    else:
        print("Invalid operation!")
        break


print(f"Total: {total_sum:.2f}")

