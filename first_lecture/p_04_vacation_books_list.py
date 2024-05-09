from math import floor
number_of_pages_current_book = int(input())
number_of_pages_per_hour = int(input())
number_of_days_per_book = int(input())

total_hours_per_book = number_of_pages_current_book / number_of_pages_per_hour
total_hours_per_day = total_hours_per_book / number_of_days_per_book

print(floor(total_hours_per_day))