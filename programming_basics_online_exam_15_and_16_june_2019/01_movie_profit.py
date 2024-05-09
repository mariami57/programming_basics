movie_name = input()
days_n = int(input())
tickets_n = int(input())
ticket_price = float(input())
cinema_percent = int(input())

total_ticket_price = ticket_price * tickets_n
total_revenue = days_n * total_ticket_price
percent_revenue = total_revenue * cinema_percent / 100
revenue_after_percent = total_revenue - percent_revenue

print(f"The profit from the movie {movie_name} is {revenue_after_percent:.2f} lv.")
