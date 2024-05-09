voucher = int(input())
purchase = input()
current_price = 0
ticket_counter = 0
others_counter = 0
while purchase != "End":
    if len(purchase) > 8:
        current_price = ord(purchase[0]) + ord(purchase[1])
        if current_price > voucher:
            break
        else:
            ticket_counter += 1
    else:
        current_price = ord(purchase[0])
        if current_price > voucher:
            break
        else:
            others_counter += 1
    voucher -= current_price
    purchase = input()

print(f"{ticket_counter}")
print(f"{others_counter}")