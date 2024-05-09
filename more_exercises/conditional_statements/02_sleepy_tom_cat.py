n_holidays = int(input())

holiday_playtime = n_holidays * 127
workdays = 365 - n_holidays
workday_playtime = workdays * 63
total_playtime = holiday_playtime + workday_playtime

diff = abs(total_playtime - 30000)
diff_hours = diff // 60
diff_minutes = diff % 60

if total_playtime > 30000:
    print("Tom will run away")
    print(f"{diff_hours} hours and {diff_minutes} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{diff_hours} hours and {diff_minutes} minutes less for play")
