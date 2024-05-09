width = int(input())
length = int(input())
height = int(input())
total_boxes = 0
free_space = width * length * height
input_line = input()
full_flag = False

while input_line != "Done":
    number_of_boxes = int(input_line)
    total_boxes += number_of_boxes

    if free_space < total_boxes:
        full_flag = True
        break

    input_line = input()

diff = abs(free_space - total_boxes)
if full_flag:
    print(f"No more free space! You need {diff} Cubic meters more.")
else:
    print(f"{diff} Cubic meters left.")


