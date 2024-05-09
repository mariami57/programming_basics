contract_duration = input()
contract_type = input()
added_mobile_data = input()
months_n = int(input())

monthly_fee = 0
if contract_duration == "one":
    if contract_type == "Small":
        monthly_fee = 9.98
    elif contract_type == "Middle":
        monthly_fee = 18.99
    elif contract_type == "Large":
        monthly_fee = 25.98
    elif contract_type == "ExtraLarge":
        monthly_fee = 35.99
elif contract_duration == "two":
    if contract_type == "Small":
        monthly_fee = 8.58
    elif contract_type == "Middle":
        monthly_fee = 17.09
    elif contract_type == "Large":
        monthly_fee = 23.59
    elif contract_type == "ExtraLarge":
        monthly_fee = 31.79


if added_mobile_data == "yes":
    if contract_type == "Small":
        monthly_fee = monthly_fee + 5.5
    elif contract_type == "Middle" or contract_type == "Large":
        monthly_fee = monthly_fee + 4.35
    elif contract_type == "ExtraLarge":
        monthly_fee = monthly_fee + 3.85

total_cost = monthly_fee * months_n
if contract_duration == "two":
    total_cost = total_cost - (total_cost * 0.0375)

print(f"{total_cost:.2f} lv.")





