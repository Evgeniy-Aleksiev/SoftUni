hall_rent = int(input())

figurines = hall_rent * 0.70
catering = figurines * 0.85
music = catering / 2
total = hall_rent + figurines + catering + music
print(f"{total:.2f}")