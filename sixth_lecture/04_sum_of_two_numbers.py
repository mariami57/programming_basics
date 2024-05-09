interval_beg = int(input())
interval_end = int(input())
magic_number = int(input())
counter_combination = 0
flag = False

for num1 in range(interval_beg, interval_end +1):
    for num2 in range(interval_beg, interval_end +1):
        counter_combination +=1
        if num1 + num2 == magic_number:
            print(f"Combination N:{counter_combination} ({num1} + {num2} = {magic_number})")
            flag = True
            break
    if flag:
        break
else:
    print(f"{counter_combination} combinations - neither equals {magic_number}")