import math

world_record = float(input())
distance = float(input())
time_per_meter = float(input())

total_time = distance * time_per_meter
delay = math.floor(distance / 15) * 12.5

total_time_with_delay = total_time + delay

diff = abs(world_record - total_time_with_delay)

if world_record > total_time_with_delay:
    print(f" Yes, he succeeded! The new world record is {total_time_with_delay:.2f} seconds.")

else:
    print(f"No, he failed! He was {diff:.2f} seconds slower.")