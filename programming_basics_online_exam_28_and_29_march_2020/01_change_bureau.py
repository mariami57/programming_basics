bitcoin_n = int(input())
cny_n = float(input())
comission_percent = float(input())

bitcoin_to_leva = bitcoin_n * 1168
cny_to_dollars = cny_n * 0.15
dollars_to_leva = cny_to_dollars * 1.76
all_to_leva = bitcoin_to_leva + dollars_to_leva
all_to_euro = all_to_leva / 1.95
comission = all_to_euro * comission_percent / 100

result = all_to_euro - comission

print(f"{result:.2f}")