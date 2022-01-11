data = input()

targeted_cities = {}

while not data == "Sail":
    city, population, gold = data.split("||")
    population = int(population)
    gold = int(gold)

    if city not in targeted_cities:
        targeted_cities[city] = {"population": population, "gold": gold}
        data = input()
        continue
    targeted_cities[city]["population"] += population
    targeted_cities[city]["gold"] += gold

    data = input()

data = input()

while not data == "End":
    com = data.split("=>")
    command = com[0]
    town = com[1]

    if command == "Plunder":
        people = int(com[2])
        stealing_gold = int(com[3])

        targeted_cities[town]["population"] -= people
        targeted_cities[town]["gold"] -= stealing_gold

        print(f"{town} plundered! {stealing_gold} gold stolen, {people} citizens killed.")

        if targeted_cities[town]["population"] <= 0 or targeted_cities[town]["gold"] <= 0:
            del targeted_cities[town]
            print(f"{town} has been wiped off the map!")

    elif command == "Prosper":
        gold_amount = int(com[2])

        if gold_amount < 0:
            print("Gold added cannot be a negative number!")
            data = input()
            continue

        targeted_cities[town]["gold"] += gold_amount
        print(f"{gold_amount} gold added to the city treasury. {town} now has {targeted_cities[town]['gold']} gold.")

    data = input()

print(f"Ahoy, Captain! There are {len(targeted_cities)} wealthy settlements to go to:")

for key, value in sorted(targeted_cities.items(), key=lambda kvp: (-kvp[1]['gold'], kvp[0])):
    print(f"{key} -> Population: {value['population']} citizens, Gold: {value['gold']} kg")
