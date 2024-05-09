stage_championship = input()
ticket_type = input()
ticket_n = int(input())
pic = input()

ticket_price = 0

if ticket_type == "Standard":
    if stage_championship == "Quarter final":
        ticket_price = 55.5
    elif stage_championship == "Semi final":
        ticket_price = 75.88
    elif stage_championship == "Final":
        ticket_price = 110.10
elif ticket_type == "Premium":
    if stage_championship == "Quarter final":
        ticket_price = 105.2
    elif stage_championship == "Semi final":
        ticket_price = 125.22
    elif stage_championship == "Final":
        ticket_price = 160.66
elif ticket_type == "VIP":
    if stage_championship == "Quarter final":
        ticket_price = 118.90
    elif stage_championship == "Semi final":
        ticket_price = 300.40
    elif stage_championship == "Final":
        ticket_price = 400

total_cost = ticket_price * ticket_n
total_cost_after_discount = 0

if total_cost > 4000:
    total_cost_after_discount = total_cost * 0.75

elif 2500 < total_cost <= 4000:
    if pic == "Y":
        total_cost_after_discount = total_cost * 0.9 + (40 * ticket_n)
    elif pic == "N":
        total_cost_after_discount = total_cost
elif total_cost < 2500:
    if pic == "Y":
        total_cost_after_discount = total_cost + (40 * ticket_n)
    elif pic == "N":
        total_cost_after_discount = total_cost


print(f"{total_cost_after_discount:.2f}")
