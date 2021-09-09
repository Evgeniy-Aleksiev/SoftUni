data = input()
people = {}

while not data == "Results":
    cmd = data.split(":")
    command = cmd[0]

    if command == "Add":
        person_name = cmd[1]
        health = int(cmd[2])
        energy = int(cmd[3])

        if person_name not in people:
            people[person_name] = {'health': 0, 'energy': energy}

        people[person_name]['health'] += health

    elif command == "Attack":
        attacker = cmd[1]
        defender = cmd[2]
        damage = int(cmd[3])

        if attacker in people and defender in people:
            people[defender]['health'] -= damage
            people[attacker]['energy'] -= 1

            if people[defender]['health'] <= 0:
                print(f"{defender} was disqualified!")
                del people[defender]

            if people[attacker]['energy'] <= 0:
                print(f"{attacker} was disqualified!")
                del people[attacker]

    elif command == "Delete":
        username = cmd[1]

        if username == "All":
            people.clear()
        elif username in people:
            del people[username]

    data = input()

print(f"People count: {len(people)}")

for key, value in sorted(people.items(), key=lambda kvp: (-kvp[1]['health'], kvp[0])):
    print(f"{key} - {value['health']} - {value['energy']}")
