pen_numbers = int(input())
marker_numbers = int(input())
preparation_litter = float(input())
discount_percent = int(input())

total_money = 0

total_money += pen_numbers * 5.80
total_money += marker_numbers * 7.20
total_money += preparation_litter * 1.20
discount = total_money - ((total_money * discount_percent) / 100)
print(f"{discount:.3f}")