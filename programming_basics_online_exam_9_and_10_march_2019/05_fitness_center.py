n_visitors = int(input())

back, chest, legs, abdomen, protein_shake, protein_bar = 0, 0, 0, 0, 0, 0

for _ in range(n_visitors):
    activity = input()
    if activity == "Back":
        back += 1
    elif activity == "Chest":
        chest += 1
    elif activity == "Legs":
        legs += 1
    elif activity == "Abs":
        abdomen += 1
    elif activity == "Protein shake":
        protein_shake += 1
    elif activity == "Protein bar":
        protein_bar += 1

percentage_people_working_out = ((back + chest + legs + abdomen) / n_visitors) * 100
percentage_buyers = ((protein_bar + protein_shake) / n_visitors) * 100

print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abdomen} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{percentage_people_working_out:.2f}% - work out")
print(f"{percentage_buyers:.2f}% - protein")
