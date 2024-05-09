inheritance = float(input())
final_year = int(input())
expenses = 0
years_turned = 18
for year in range(1800, final_year+1):

    if year % 2 == 0:
        expenses = 12000
    else:
        expenses = 12000 + (50 * years_turned)

    inheritance -= expenses
    years_turned += 1
inheritance_abs = abs(inheritance)
if inheritance >= 0:
    print(f"Yes! He will live a carefree life and will have {inheritance_abs:.2f} dollars left.")
else:
    print(f"He will need {inheritance_abs:.2f} dollars to survive." )