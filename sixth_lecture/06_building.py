floor_number = int(input())
rooms_per_floor = int(input())

room_type = ""
for floor in reversed(range(1,floor_number + 1)):
    for room in range(0, rooms_per_floor):

        if floor == floor_number:
            room_type = "L"
        elif floor % 2 == 0:
            room_type = "O"
        else:
            room_type = "A"

        print(f"{room_type}{floor}{room}", end=" ")
    print()





