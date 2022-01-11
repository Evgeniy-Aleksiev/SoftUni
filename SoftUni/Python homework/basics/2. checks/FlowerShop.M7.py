from math import ceil

number_of_magnolias = int(input())      # магнолий 3,25
number_of_hyacinths = int(input())      # зюмбюл 4
number_of_roses = int(input())          # рози 3,50
number_of_cacti = int(input())          # кактус 8
price_of_the_gift = float(input())        # цена на подарък

sum = number_of_magnolias * 3.25 + number_of_hyacinths * 4 + number_of_roses * 3.50 + number_of_cacti * 8
tax = sum - sum * 0.05

if tax >= price_of_the_gift:
    money_left = tax - price_of_the_gift
    print(f"She is left with {int(money_left)} leva.")
else:
    money_need = price_of_the_gift - tax
    print(f"She will have to borrow {ceil(money_need)} leva.")