n = int(input())

current_number = 0

while n >= current_number:
    current_number = 2 * current_number + 1

    if current_number > n:
        break

    print(current_number)
