n_days = int(input())
total_win = 0
total_loss = 0
total_money_won = 0
for i in range(1, n_days+1):
    sport = input()
    current_win = 0
    current_loss = 0
    money_per_win = 0
    while sport != "Finish":
        result = input()
        if result == "win":
            current_win += 1
            total_win += 1
            money_per_win += 20
        else:
            current_loss += 1
            total_loss += 1

        sport = input()
    if current_win > current_loss:
        money_per_win = money_per_win * 1.1
    total_money_won += money_per_win

if total_win > total_loss:
    total_money_won = total_money_won * 1.2
    print(f"You won the tournament! Total raised money: {total_money_won:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money_won:.2f}")





