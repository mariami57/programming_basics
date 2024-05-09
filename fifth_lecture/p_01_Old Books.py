book = input()
counter = 0
current_book = input()
missing_book = False

while current_book != book:

    if current_book == "No More Books":
        missing_book = True
        break

    counter += 1
    current_book = input()


if missing_book:
    print("The book you search is not here!")
    print(f"You checked {counter} books.")
else:
    print(f"You checked {counter} books and found it.")



