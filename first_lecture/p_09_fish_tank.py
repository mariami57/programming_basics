length = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume_fish_tank_centimeters = length * width * height
volume_fish_tank_decimeters =volume_fish_tank_centimeters * 0.001
filled_space = percent/100

needed_litres = volume_fish_tank_decimeters * (1 - filled_space)

print(needed_litres)
