type_screening = input()
rows_n = int(input())
columns_n = int(input())

cinema_capacity = rows_n * columns_n
revenue = 0

if type_screening == "Premiere":
    revenue = cinema_capacity * 12

elif type_screening == "Normal":
    revenue = cinema_capacity * 7.5

elif type_screening == "Discount":
    revenue = cinema_capacity * 5

print(f"{revenue:.2f} leva")
