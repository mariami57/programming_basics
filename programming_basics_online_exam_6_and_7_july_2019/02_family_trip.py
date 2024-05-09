budget = float(input())
stays_n = int(input())
stay_price = float(input())
additional_expenses_percent = int(input())

if stays_n > 7:
   stay_price = stay_price * 0.95

stays_cost = stays_n * stay_price

additional_expenses = budget * additional_expenses_percent / 100

total_expense = stays_cost + additional_expenses

diff = abs(total_expense - budget)

if total_expense <= budget:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")

else:
    print(f"{diff:.2f} leva needed.")