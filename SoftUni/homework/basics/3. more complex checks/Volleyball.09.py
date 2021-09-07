year = input()
holidays = int(input())
weekends = int(input())

travel_to_home = 48 - weekends
saturday_in_sofia = (travel_to_home * 3) / 4
holiday_in_sofia = (holidays * 2) / 3
total_games = saturday_in_sofia + weekends + holiday_in_sofia

if year == "leap":
    sum = total_games * 0.15
    games = int(total_games + sum)
    print(games)
else:
    print(int(total_games))