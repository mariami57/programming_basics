import sys

min_number = sys.maxsize

while True:
    data = input()

    if data == "Stop":
        print(min_number)
        break

    current_number = int(data)
    if current_number < min_number:
        min_number = current_number
