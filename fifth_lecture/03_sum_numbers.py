number = int(input())

numbers_sum = 0
while True:
    current_number = int(input())
    numbers_sum += current_number

    if numbers_sum >= number:
        print(numbers_sum)
        break
