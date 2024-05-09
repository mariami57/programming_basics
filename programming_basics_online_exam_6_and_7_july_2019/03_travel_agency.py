city = input()
package_type = input()
vip_discount = input()
days_of_stay = int(input())

price_per_day = 0
wrong_data = False

if city == "Bansko" or city == "Borovets":
    if package_type == "withEquipment" and vip_discount == "yes":
        price_per_day = 90
    elif package_type == "withEquipment" and vip_discount == "no":
        price_per_day = 100
    elif package_type == "noEquipment" and vip_discount == "yes":
        price_per_day = 76
    elif package_type == "noEquipment" and vip_discount == "no":
        price_per_day = 80
    else:
        wrong_data = True


elif city == "Varna" or city == "Burgas":
    if package_type == "withBreakfast" and vip_discount == "yes":
        price_per_day = 130 * 0.88
    elif package_type == "withBreakfast" and vip_discount == "no":
        price_per_day = 130
    elif package_type == "noBreakfast" and vip_discount == "yes":
        price_per_day = 100 * 0.93
    elif package_type == "noBreakfast" and vip_discount == "no":
        price_per_day = 100
    else:
        wrong_data = True

else:
    wrong_data = True

if wrong_data:
    print("Invalid input!")

total_price = price_per_day * days_of_stay

if days_of_stay > 7:
    total_price = price_per_day * (days_of_stay - 1)

if days_of_stay < 1:
    print("Days must be positive number!")
elif days_of_stay > 1 and wrong_data is False:
    print(f"The price is {total_price:.2f}lv! Have a nice time!")
