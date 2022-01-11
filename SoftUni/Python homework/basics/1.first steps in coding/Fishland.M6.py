mackerel_price = float(input())#скумрия
sprat_price = float(input())# цаца
bonito_kg = float(input())# паламуд
scad_kg = float(input())# сафрид
mussels_kg = int(input())# миди
bonito_price = mackerel_price + mackerel_price * 60 / 100
scad_price = sprat_price + sprat_price * 80 / 100
mussels_price = 7.50
bonito_sum = bonito_price * bonito_kg
scad_sum = scad_price * scad_kg
mussels_sum = mussels_price * mussels_kg
total_sum = bonito_sum + scad_sum + mussels_sum
print(round(total_sum, 2))
