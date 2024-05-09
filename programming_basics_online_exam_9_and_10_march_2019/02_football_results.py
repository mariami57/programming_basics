first_game = input()
second_game = input()
third_game = input()
# host_goals = 0
# guest_goals = 0
result = ""

# first_game == f"{host_goals}:{guest_goals}"

if host_goals > guest_goals:
    result = "win"

elif host_goals < guest_goals:
    result = "lose"

elif host_goals == guest_goals:
    result = "drawn"

# three_matches

print(result)





