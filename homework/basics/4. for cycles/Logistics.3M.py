number = int(input())
price_minibus = 0
price_truck = 0
price_train = 0
sum_minibus = 0
sum_truck = 0
sum_train = 0

for tonnage_cargo in range(number):
    tonnage_cargo = int(input())
    if tonnage_cargo < 4:
        price_minibus += tonnage_cargo * 200
        sum_minibus += tonnage_cargo
    elif tonnage_cargo < 12:
        price_truck += tonnage_cargo * 175
        sum_truck += tonnage_cargo
    else:
        price_train += tonnage_cargo * 120
        sum_train += tonnage_cargo

total_transport = sum_minibus + sum_truck + sum_train
total_price = (price_minibus + price_truck + price_train) / total_transport
print(f"{total_price:.2f}")
minibus = sum_minibus / total_transport * 100
print(f"{minibus:.2f}%")
truck = sum_truck / total_transport * 100
print(f"{truck:.2f}%")
train = sum_train / total_transport * 100
print(f"{train:.2f}%")