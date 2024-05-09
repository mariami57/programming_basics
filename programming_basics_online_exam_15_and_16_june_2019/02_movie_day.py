shooting_time = int(input())
scenes_n = int(input())
scene_time = int(input())

preparation = shooting_time * 0.15
total_scene_time = scene_time * scenes_n
time_shooting_day = total_scene_time + preparation

diff = time_shooting_day - shooting_time
rounded_diff = round(abs(diff))

if shooting_time >= time_shooting_day:
    print(f"You managed to finish the movie on time! You have {rounded_diff} minutes left!")

else:
    print(f"Time is up! To complete the movie you need {rounded_diff} minutes.")