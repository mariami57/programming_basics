import math

record = float(input())
distance = float(input())
time_per_meter = float(input())

total_time = distance * time_per_meter
delay = math.floor(distance / 50) * 30

total_time_with_delay = total_time + delay

diff = abs(total_time_with_delay - record)

if total_time_with_delay >= record:
    print(f"No! He was {diff:.2f} seconds slower.")

else:
    print(f" Yes! The new record is {total_time_with_delay:.2f} seconds.")