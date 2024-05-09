tabs_number = int(input())
salary = int(input())

facebook = 0
instagram = 0
reddit = 0


for _ in range(tabs_number):
    website = input()
    if website == "Facebook":
        salary -= 150
    elif website == "Instagram":
        salary -= 100
    elif website == "Reddit":
        salary -= 50

    if salary == 0:
        print("You have lost your salary.")
        break
else:
    print(salary)

