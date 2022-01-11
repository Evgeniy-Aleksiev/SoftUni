bitcoin_number = int(input())
chinese_juan = float(input())
commission = float(input())

lev = 0
dollars = 0
euro = 0

lev += bitcoin_number * 1168
dollars += chinese_juan * 0.15
lev += dollars * 1.76
euro += lev / 1.95
total_commission = commission / 100 * euro
result = euro - total_commission

print(f"{result:.2f}")

