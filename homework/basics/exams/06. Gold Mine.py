number_location = int(input())

for location in range(number_location):
    expected_average_yield = float(input())  # Очакван среден добив на ден злато
    dig_in_days = int(input())       # Брой дни в които ще се копае
    gold_mining = 0                 # Общ добив
    for days in range(dig_in_days):
        gold_mined = float(input())   # Добито злато на ден
        gold_mining += gold_mined

    average_gold_mined = gold_mining / dig_in_days
    if expected_average_yield <= average_gold_mined:
        print(f"Good job! Average gold per day: {average_gold_mined:.2f}.")
    else:
        gold_need = expected_average_yield - average_gold_mined
        print(f"You need {gold_need:.2f} gold.")

