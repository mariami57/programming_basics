budget = float(input())
actor = input()
name_length = len(actor)

while actor != "ACTION":
    if name_length <= 15:
        salary = float(input())
    else:
        salary = 0.2 * budget

    budget -= salary
    if budget <= 0:
        break

    actor = input()
    name_length = len(actor)

budget_abs = abs(budget)
if budget <= 0:
    print(f"We need {budget_abs:.2f} leva for our actors.")
else:
    print(f"We are left with {budget_abs:.2f} leva.")


