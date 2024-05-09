deposit = float(input())
deposit_duration = int(input())
annual_interest = float(input())

total_interest = deposit * (annual_interest/100)
monthly_interest = total_interest / 12
total_savings = deposit + deposit_duration * ((deposit * (annual_interest/100))/12)

print(total_savings)