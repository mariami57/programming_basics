import math

series_name = input()
episode_duration = int(input())
break_duration = int(input())

lunch = break_duration / 8
relax = break_duration / 4

break_time_left = break_duration - lunch - relax

diff = abs(break_time_left-episode_duration)
rounded_diff = math.ceil(diff)

if break_time_left >= episode_duration:
    print(f"You have enough time to watch {series_name} and left with {rounded_diff} minutes free time.")

else:
    print(f"You don't have enough time to watch {series_name}, you need {rounded_diff} more minutes.")