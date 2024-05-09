basketball_annual_fee = int(input())

shoes = basketball_annual_fee - (basketball_annual_fee * 0.4)
suit = shoes - (shoes * 0.2)
ball = suit / 4
accessories = ball / 5

total_expenses = basketball_annual_fee + shoes + suit + ball + accessories

print(total_expenses)