desired_profit = float(input())
cocktail_name = input()
total_revenue = 0

while cocktail_name != "Party!":
    n_cocktails = int(input())

    cocktail_price = len(cocktail_name)
    revenue_from_cocktail = cocktail_price * n_cocktails
    if revenue_from_cocktail % 2 != 0:
        revenue_from_cocktail *= 0.75

    total_revenue += revenue_from_cocktail
    if total_revenue >= desired_profit:
        break
    cocktail_name = input()

diff = abs(desired_profit - total_revenue)

if total_revenue >= desired_profit:
    print("Target acquired.")
    print(f"Club income - {total_revenue:.2f} leva.")
else:
    print(f"We need {diff:.2f} leva more.")
    print(f"Club income - {total_revenue:.2f} leva.")



