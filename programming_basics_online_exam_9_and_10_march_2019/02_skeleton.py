control_min = int(input())
control_sec = int(input())
length_metres = float(input())
sec_per_100_metres = int(input())

control_total_secs = (control_min * 60) + control_sec
time_decrease = length_metres / 120
time_decrease_total = time_decrease * 2.5
competitor_time = (length_metres / 100) * sec_per_100_metres - time_decrease_total

diff = abs(competitor_time - control_total_secs)

if control_total_secs >= competitor_time:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {competitor_time:.3f}.")

else:
    print(f"No, Marin failed! He was {diff:.3f} second slower.")