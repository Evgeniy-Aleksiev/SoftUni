n = int(input())

max_tank_fuel = 75
cars_obtain = {}

for _ in range(n):
    cars, mileage, fuel_available = input().split("|")
    mileage = int(mileage)
    fuel_available = int(fuel_available)
    cars_obtain[cars] = {'mileage': mileage, 'fuel': fuel_available}

data = input()

while not data == "Stop":
    cmd = data.split(" : ")
    command = cmd[0]
    car = cmd[1]

    if command == "Drive":
        distance = int(cmd[2])
        fuel = int(cmd[3])

        if cars_obtain[car]['fuel'] < fuel:
            print("Not enough fuel to make that ride")
            data = input()
            continue

        cars_obtain[car]['mileage'] += distance
        cars_obtain[car]['fuel'] -= fuel
        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

        if cars_obtain[car]['mileage'] >= 100_000:
            print(f"Time to sell the {car}!")
            del cars_obtain[car]

    elif command == "Refuel":
        fuel = int(cmd[2])

        current_fuel = cars_obtain[car]['fuel']
        current_fuel += fuel
        if current_fuel > 75:
            amount = 75 - cars_obtain[car]['fuel']
            cars_obtain[car]['fuel'] += amount
            print(f"{car} refueled with {amount} liters")
            data = input()
            continue

        cars_obtain[car]['fuel'] += fuel
        print(f"{car} refueled with {fuel} liters")

    elif command == "Revert":
        km = int(cmd[2])

        cars_obtain[car]['mileage'] -= km
        if cars_obtain[car]['mileage'] < 10_000:
            cars_obtain[car]['mileage'] = 10_000
            data = input()
            continue

        print(f"{car} mileage decreased by {km} kilometers")
    data = input()

for key, value in sorted(cars_obtain.items(), key=lambda kvp: (-kvp[1]['mileage'], kvp[0])):
    print(f"{key} -> Mileage: {value['mileage']} kms, Fuel in the tank: {value['fuel']} lt.")

