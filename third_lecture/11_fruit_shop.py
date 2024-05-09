fruit = input()
day = input()
quantity = float(input())

fruit_price = 0

wrong_data = False

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    if fruit == "banana":
        fruit_price = 2.5
    elif fruit == "apple":
        fruit_price = 1.2
    elif fruit == "orange":
        fruit_price = 0.85
    elif fruit == "grapefruit":
        fruit_price = 1.45
    elif fruit == "kiwi":
        fruit_price = 2.7
    elif fruit == "pineapple":
        fruit_price = 5.5
    elif fruit == "grapes":
        fruit_price = 3.85
    else:
        wrong_data = True

elif day == "Saturday" or day == "Sunday":
    if fruit == "banana":
        fruit_price = 2.7
    elif fruit == "apple":
        fruit_price = 1.25
    elif fruit == "orange":
        fruit_price = 0.90
    elif fruit == "grapefruit":
        fruit_price = 1.60
    elif fruit == "kiwi":
        fruit_price = 3
    elif fruit == "pineapple":
        fruit_price = 5.6
    elif fruit == "grapes":
        fruit_price = 4.2
    else:
        wrong_data = True

else:
    wrong_data = True

if wrong_data:
    print("error")

total_cost = quantity * fruit_price

if total_cost !=0 :
    print(f"{total_cost:.2f}")








