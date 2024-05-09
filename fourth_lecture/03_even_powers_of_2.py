number = int(input())


for number in range(0, number+1):
    if number % 2 == 0:
        total = 2 ** number
        print(total)

