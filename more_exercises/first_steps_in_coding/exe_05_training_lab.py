h_metres = float(input())
w_metres = float(input())


width_cm = w_metres * 100
hallway_width_cm = 100
space_for_desks_width = width_cm - hallway_width_cm
number_of_desks = space_for_desks_width // 70

height_cm = h_metres * 100
space_for_desks_height = height_cm // 120

number_of_workspaces = number_of_desks * space_for_desks_height - 3

print(number_of_workspaces)
