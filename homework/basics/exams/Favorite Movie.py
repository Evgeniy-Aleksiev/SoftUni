import sys

command = input()
movies_count = 0
max_points = -sys.maxsize
favorite_movie = " "
limit_movie_reached = False

while command != "STOP":
    movie_name = command
    letter_count = 0
    points = 0
    movies_count += 1
    for letter in range(len(movie_name)):
        letter_count += 1
    for char in movie_name:
        letter_points = ord(char)
        if 97 <= letter_points <= 122:
            points += letter_points - letter_count * 2
        elif 65 <= letter_points <= 90:
            points += letter_points - letter_count
        else:
            points += letter_points
    if points > max_points:
        max_points = points
        favorite_movie = movie_name
    if movies_count >= 7:
        limit_movie_reached = True
        break
    command = input()

if limit_movie_reached:
    print("The limit is reached.")
print(f"The best movie for you is {favorite_movie} with {max_points} ASCII sum.")
