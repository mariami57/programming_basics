n = int(input())

left_sum = 0
right_sum = 0


for i in range(1, n+1):
    left_sum = left_sum + int(input())

for i in range(1, n+1):
    right_sum = right_sum + int(input())

diff = abs(left_sum - right_sum)

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {diff}")
