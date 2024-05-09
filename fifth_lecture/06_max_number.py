import sys

max_number = -sys.maxsize

while True:
    data = input()

    if data == "Stop":
        print(max_number)
        break

    current_number = int(data)
    if current_number > max_number:
        max_number = current_number






