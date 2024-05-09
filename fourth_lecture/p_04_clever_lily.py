age_of_lily = int(input())
washing_machine_price = float(input())
toy_price = int(input())

saved_money = 0
toy_count = 0
brother_money = 0

for birthday in range(1, age_of_lily + 1):
    if birthday % 2 == 0:
        saved_money += 10 * (birthday // 2)
        brother_money += 1

    else:
        toy_count += 1

total_savings_from_toys = toy_count * toy_price
total_savings = total_savings_from_toys + saved_money - brother_money

diff = abs(total_savings - washing_machine_price)

if total_savings >= washing_machine_price:
    print(f"Yes! {diff:.2f}")

else:
    print(f"No! {diff:.2f}")
