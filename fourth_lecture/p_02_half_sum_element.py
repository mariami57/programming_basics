import sys

n = int(input())
max_number = -sys.maxsize
total_sum = 0

for _ in range(n):
    current_number = int(input())

    total_sum += current_number

    if current_number > max_number:
        max_number = current_number


diff = abs(max_number - (total_sum - max_number))

if total_sum - max_number == max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    print("No")
    print(f"Diff = {diff}")
