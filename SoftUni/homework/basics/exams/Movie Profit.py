movie_name = input()
project_days = int(input())
ticket_count = int(input())
ticket_price = float(input())
percent = int(input())

total_ticket_price_per_day = ticket_price * ticket_count
total_profit = project_days * total_ticket_price_per_day
cinema_percent = total_profit * percent / 100
movie_profit = total_profit - cinema_percent

print(f"The profit from the movie {movie_name} is {movie_profit:.2f} lv.")