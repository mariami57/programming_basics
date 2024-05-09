groups_number = int(input())

musala, monblan, kilimanjaro, k2, everest = 0, 0, 0, 0, 0

for _ in range(groups_number):
    n_people = int(input())
    if n_people <= 5:
        musala += n_people
    elif 6 <= n_people <= 12:
        monblan += n_people
    elif 13 <= n_people <= 25:
        kilimanjaro += n_people
    elif 26 <= n_people <= 40:
        k2 += n_people
    elif n_people >= 41:
        everest += n_people

total_number_of_climbers = musala + monblan + kilimanjaro + k2 + everest

musala_percentage = musala / total_number_of_climbers * 100
monblan_percentage = monblan / total_number_of_climbers * 100
kilimanjaro_percentage = kilimanjaro / total_number_of_climbers * 100
k2_percentage = k2 / total_number_of_climbers * 100
everest_percentage = everest / total_number_of_climbers * 100


print(f"{musala_percentage:.2f}%")
print(f"{monblan_percentage:.2f}%")
print(f"{kilimanjaro_percentage:.2f}%")
print(f"{k2_percentage:.2f}%")
print(f"{everest_percentage:.2f}%")