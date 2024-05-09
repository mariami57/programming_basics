city = input()
trade_volume = float(input())

commission = 0
wrong_data = False

if city == "Sofia":
    if 0 <= trade_volume <= 500:
        commission = trade_volume * 0.05
    elif 500 < trade_volume <= 1000:
        commission = trade_volume * 0.07
    elif 1000 < trade_volume <= 10000:
        commission = trade_volume * 0.08
    elif trade_volume > 10000:
        commission = trade_volume * 0.12
    else:
        wrong_data = True

elif city == "Varna":
    if 0 <= trade_volume <= 500:
        commission = trade_volume * 0.045
    elif 500 < trade_volume <= 1000:
        commission = trade_volume * 0.075
    elif 1000 < trade_volume <= 10000:
        commission = trade_volume * 0.1
    elif trade_volume > 10000:
        commission = trade_volume * 0.13
    else:
        wrong_data = True

elif city == "Plovdiv":
    if 0 <= trade_volume <= 500:
        commission = trade_volume * 0.055
    elif 500 < trade_volume <= 1000:
        commission = trade_volume * 0.08
    elif 1000 < trade_volume <= 10000:
        commission = trade_volume * 0.12
    elif trade_volume > 10000:
        commission = trade_volume * 0.145
    else:
        wrong_data = True

else:
    wrong_data = True

if wrong_data:
    print("error")
else:
    print(f"{commission:.2f}")
# commission_sum = commission * trade_volume

# if commission_sum != 0:
#     print(f"{commission_sum:.2f}")
# else:
#     print("error")