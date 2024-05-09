company = input()
adult_tickets_n = int(input())
kid_tickets_n = int(input())
adult_ticket_price = float(input())
tax = float(input())

kid_ticket_price = adult_ticket_price * 0.3
adult_ticket_with_tax = adult_ticket_price + tax
kid_ticket_with_tax = kid_ticket_price + tax
total_revenue = (adult_ticket_with_tax * adult_tickets_n) + (kid_ticket_with_tax * kid_tickets_n)
profit = 0.2 * total_revenue

print(f"The profit of your agency from {company} tickets is {profit:.2f} lv.")