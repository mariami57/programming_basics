first = int(input())
second = int(input())
third = int(input())

total_time_secs = first + second + third
minutes = total_time_secs // 60
seconds = total_time_secs % 60

if seconds < 10:
    print(f"{minutes}:0{seconds}")

else:
    print(f"{minutes}:{seconds}")