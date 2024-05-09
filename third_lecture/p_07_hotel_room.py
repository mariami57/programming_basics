month = input()
n_stays = int(input())

studio_price = 0
apartment_price = 0

if month == "May" or month == "October":
    if n_stays <= 7:
        studio_price = 50 * n_stays
        apartment_price = 65 * n_stays
    elif 7 < n_stays <= 14:
        studio_price = (50 * n_stays) * 0.95
        apartment_price = 65 * n_stays
    elif n_stays > 14:
        studio_price = (50 * n_stays) * 0.7
        apartment_price = (65 * n_stays) * 0.9

elif month == "June" or month == "September":
    if n_stays <= 14:
        studio_price = 75.2 * n_stays
        apartment_price = 68.7 * n_stays
    elif n_stays > 14:
        studio_price = (75.2 * n_stays) * 0.8
        apartment_price = (68.7 * n_stays) * 0.9

elif month == "July" or month == "August":
    if n_stays <= 14:
        studio_price = 76 * n_stays
        apartment_price = 77 * n_stays
    elif n_stays > 14:
        studio_price = 76 * n_stays
        apartment_price = (77 * n_stays) * 0.9

print(f"Apartment: {apartment_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")