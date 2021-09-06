# Подаръка който купи зависи от възрастта на хората
# Всички до 16г. се считат за деца и получават играчка
# Всички над 16 се считат за възрастни и ще получат коледен пуловер
# Цената на всяка играчка е 5лв, а пуловер е 15лв

command = input()
adults = 0
kids = 0
money_for_toys = 0
money_for_sweaters = 0

while command != "Christmas":
    age = int(command)
    if age <= 16:
        kids += 1
        money_for_toys += 5
    else:
        adults += 1
        money_for_sweaters += 15
    command = input()
print(f"Number of adults: {adults}" )
print(f"Number of kids: {kids}")
print(f"Money for toys: {money_for_toys}")
print(f"Money for sweaters: {money_for_sweaters}")