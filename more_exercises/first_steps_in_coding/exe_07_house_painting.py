x = float(input())
y = float(input())
h = float(input())

side_wall = x * y
window = 1.5 ** 2
both_side_walls_area_without_windows = side_wall * 2 - 2 * window
other_wall = x ** 2
door = 1.2 * 2
front_and_back_walls_area_without_entrance = other_wall * 2 - door
total_house_area = front_and_back_walls_area_without_entrance + both_side_walls_area_without_windows

green_paint_litres = total_house_area / 3.4

roof_two_sides = 2 * (x * y)
roof_front_and_back = 2 * (x * h/2)

roof_area = roof_two_sides + roof_front_and_back

red_paint_litres = roof_area / 4.3

print(f"{green_paint_litres:.2f}")
print(f"{red_paint_litres:.2f}")
