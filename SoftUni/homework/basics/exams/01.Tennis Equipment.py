import math

price_tennis_racket = float(input())
number_tennis_rackets = int(input())
number_socks = int(input())

# Цена на тенис ракети -> price_tennis_rackets * number
# Цена за маратонки -> price_tennis_rackets 1/6
# Цена за друга екипировка -> 20% от общата цена на закупените ракети и маратонки
# Крайната цена се сформира от сумата на ракетите, маратонките и останалите екипировки
# Джокович трябва да заплати 1/8 от цената
# Спонсори трябва да заплатят 7/8

total_price_rackets = price_tennis_racket * number_tennis_rackets
total_price_socks = number_socks * (price_tennis_racket / 6)
total_price_other_equipment = 0.20 * (total_price_socks + total_price_rackets)

total_price = total_price_rackets + total_price_socks + total_price_other_equipment
djokovic = total_price / 8
sponsors = total_price * 7 / 8
print(f"Price to be paid by Djokovic {math.floor(djokovic)}")
print(f"Price to be paid by sponsors {math.ceil(sponsors)}")