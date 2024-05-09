init_hour = int(input())
init_minutes = int(input())

total_time = (init_hour * 60) + init_minutes + 15

hour = total_time // 60
minutes = total_time % 60

if hour > 23:
    hour = 0

print(f"{hour}:{minutes:02}")

hour = int(input())
minutes = int(input())

hour_in_minutes = hour * 60
total_time_minutes = hour_in_minutes + minutes + 15
total_time_hours = total_time_minutes // 60
final_minutes = total_time_minutes % 60

if total_time_hours > 23:
    total_time_hours = 0

if final_minutes >= 10:
    print(f"{total_time_hours}:{final_minutes}")

else:
    print(f"{total_time_hours}:0{final_minutes}")




