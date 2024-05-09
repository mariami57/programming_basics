import sys

movies_n = int(input())

highest_rating = - sys.maxsize
lowest_rating = sys.maxsize
middle_rating = 0
sum_ratings = 0
movie_highest_rating = ""
movie_lowest_rating = ""

for _ in range(movies_n):
    current_movie = input()
    current_rating = float(input())
    if current_rating > highest_rating:
        highest_rating = current_rating
        movie_highest_rating = current_movie

    elif current_rating < lowest_rating:
        lowest_rating = current_rating
        movie_lowest_rating = current_movie

    sum_ratings += current_rating

middle_rating = sum_ratings / movies_n


print(f"{movie_highest_rating} is with highest rating: {highest_rating}")
print(f"{movie_lowest_rating} is with lowest rating: {lowest_rating}")
print(f"Average rating: {middle_rating:.1f}")


