movie_title = input()
counter = 0

best_movie = ""
best_ascii_score = 0

while movie_title != "STOP":
    counter += 1
    ascii_counter = 0
    if counter == 7:
        print("The limit is reached.")
        break
    for letter in movie_title:
        current_ascii_value = ord(letter)
        if 65 <= ord(letter) <= 90:
            current_ascii_value -= len(movie_title)
        elif 97 <= ord(letter) <= 122:
            current_ascii_value -= 2 * len(movie_title)

        ascii_counter += current_ascii_value

        if ascii_counter > best_ascii_score:
            best_ascii_score = ascii_counter
            best_movie = movie_title
    movie_title = input()
print(f"The best movie for you is {best_movie} with {best_ascii_score} ASCII sum.")

