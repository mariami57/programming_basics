first_player_eggs = int(input())
second_player_eggs = int(input())

result = input()
no_eggs = False
while result != "End":
    if result == "one":
        second_player_eggs -= 1
    elif result == "two":
        first_player_eggs -= 1

    if first_player_eggs == 0 or second_player_eggs == 0:
        no_eggs = True
        break

    result = input()

if no_eggs:
    if first_player_eggs == 0:
        print(f"Player one is out of eggs. Player two has {second_player_eggs} eggs left.")
    elif second_player_eggs == 0:
        print(f"Player two is out of eggs. Player one has {first_player_eggs} eggs left.")
else:
    print(f"Player one has {first_player_eggs} eggs left.")
    print(f"Player two has {second_player_eggs} eggs left.")


