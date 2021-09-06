strawberries_price = float(input())
banana_quantity = float(input())
orange_quantity = float(input())
raspberries_quantity = float(input())
strawberries_quantity = float(input())

raspberries_price = strawberries_price / 2
orange_price = raspberries_price * 0.60
banana_price = raspberries_price * 0.20

sum = raspberries_quantity * raspberries_price + orange_price * orange_quantity +\
    banana_price * banana_quantity + strawberries_quantity * strawberries_price

print(sum)