n_seats = int(input())
input_line = input()
ticket_price = 5
seats_counter = 0
full = False
accrued_revenue = 0

while input_line != "Movie time!":
    n_people = int(input_line)
    seats_counter += n_people
    total_revenue = n_people * ticket_price

    if n_people % 3 == 0:
        total_revenue -= ticket_price

    if seats_counter > n_seats:
        full = True
        break

    accrued_revenue += total_revenue
    input_line = input()

diff = abs(n_seats - seats_counter)
if full:
    print("The cinema is full.")
    print(f"Cinema income - {accrued_revenue} lv.")
else:
    print(f"There are {diff} seats left in the cinema.")
    print(f"Cinema income - {accrued_revenue} lv.")






