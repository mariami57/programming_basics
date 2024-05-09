exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_total_minutes = (exam_hour * 60) + exam_minute
arrival_total_minutes = (arrival_hour * 60) + arrival_minute

diff_min = abs(arrival_total_minutes - exam_total_minutes)

if arrival_total_minutes > exam_total_minutes:
    print("Late")
    if diff_min < 60:
        print(f"{diff_min} minutes after the start" )
    else:
        hour = diff_min // 60
        minutes = diff_min % 60
        print(f"{hour}:{minutes:02d} hours after the start")
elif arrival_total_minutes == exam_total_minutes or diff_min <= 30:
    print("On time")
    if diff_min > 0:
        print(f"{diff_min} minutes before the start")
elif arrival_total_minutes < exam_total_minutes:
    print("Early")
    if diff_min < 60:
        print(f"{diff_min} minutes before the start")
    else:
        hour = diff_min // 60
        minutes = diff_min % 60
        print(f"{hour}:{minutes:02d} hours before the start")

