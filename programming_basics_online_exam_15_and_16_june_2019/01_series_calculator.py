import math

series_name = input()
seasons_n = int(input())
episodes_n = int(input())
time_of_episode_without_commercials = float(input())

commercials_duration = time_of_episode_without_commercials * 0.2
time_of_episode_with_commercials = commercials_duration + time_of_episode_without_commercials
added_time_special_episodes_total = seasons_n * 10
series_total_time = time_of_episode_with_commercials * seasons_n * episodes_n + added_time_special_episodes_total

series_total_time_rounded = math.floor(series_total_time)

print(f"Total time needed to watch the {series_name} series is {series_total_time_rounded} minutes.")