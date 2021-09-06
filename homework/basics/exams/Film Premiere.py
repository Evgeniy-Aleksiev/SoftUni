movie_name = input()
movie_packet = input()
ticket_number = int(input())

ticket_price = 0

if movie_name == "John Wick":
    if movie_packet == "Drink":
        ticket_price = 12
    elif movie_packet == "Popcorn":
        ticket_price = 15
    elif movie_packet == "Menu":
        ticket_price = 19
    ticket_price *= ticket_number
elif movie_name == "Star Wars":
    if movie_packet == "Drink":
        ticket_price = 18
    elif movie_packet == "Popcorn":
        ticket_price = 25
    elif movie_packet == "Menu":
        ticket_price = 30
    ticket_price *= ticket_number
    if ticket_number >= 4:
        ticket_price *= 0.70
elif movie_name == "Jumanji":
    if movie_packet == "Drink":
        ticket_price = 9
    elif movie_packet == "Popcorn":
        ticket_price = 11
    elif movie_packet == "Menu":
        ticket_price = 14
    ticket_price *= ticket_number
    if ticket_number == 2:
        ticket_price *= 0.85

print(f"Your bill is {ticket_price:.2f} leva.")

