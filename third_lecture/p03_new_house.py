flower = input()
n_flower = int(input())
budget = int(input())

total_sum = 0

if flower == "Roses":
    if n_flower > 80:
        total_sum = (n_flower * 5) * 0.9
    else:
        total_sum = n_flower * 5
elif flower == "Dahlias":
    if n_flower > 90:
        total_sum = (n_flower* 3.8) * 0.85
    else:
        total_sum = n_flower * 3.8
elif flower == "Tulips":
   if n_flower > 80:
       total_sum = (n_flower * 2.8) * 0.85
   else:
       total_sum = n_flower * 2.8
elif flower == "Narcissus":
    if n_flower < 120:
        total_sum = (n_flower * 3) * 1.15
    else:
        total_sum = n_flower * 3
elif flower == "Gladiolus":
    if n_flower < 80:
        total_sum = (n_flower * 2.5) * 1.2
    else:
        total_sum = n_flower * 2.5

diff = abs(total_sum - budget)
if budget >= total_sum:
    print(f"Hey, you have a great garden with {n_flower} {flower} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")


