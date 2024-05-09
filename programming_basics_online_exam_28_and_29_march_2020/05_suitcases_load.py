capacity = float(input())
input_line = input()
counter = 0
limit_reached = False
while input_line != "End":
    suitcase_volume = float(input_line)
    counter += 1
    if counter % 3 == 0:
        suitcase_volume *= 1.1

    if capacity < suitcase_volume or capacity <= 0:
        counter -= 1
        limit_reached = True
        break

    capacity = capacity - suitcase_volume

    input_line = input()

if limit_reached:
    print("No more space!")
    print(f"Statistic: {counter} suitcases loaded.")
else:
    print("Congratulations! All suitcases are loaded!")
    print(f"Statistic: {counter} suitcases loaded.")