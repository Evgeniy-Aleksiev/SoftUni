n = int(input())

max_hp, max_mp = 100, 200
heroes = {}

for _ in range(n):
    hero_name, hp, mp = input().split()
    heroes[hero_name] = {'hp': int(hp), 'mp': int(mp)}

data = input()

while not data == "End":
    command = data.split(" - ")
    cmd = command[0]
    hero = command[1]

    if cmd == "CastSpell":
        mp_need = int(command[2])
        spell_name = command[3]
        if heroes[hero]['mp'] >= mp_need:
            heroes[hero]['mp'] -= mp_need
            print(f"{hero} has successfully cast {spell_name} and now has {heroes[hero]['mp']} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell_name}!")
    elif cmd == "TakeDamage":
        damage = int(command[2])
        attacker = command[3]
        heroes[hero]['hp'] -= damage
        if heroes[hero]['hp'] > 0:
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {heroes[hero]['hp']} HP left!")
        else:
            print(f"{hero} has been killed by {attacker}!")
            del heroes[hero]
    elif cmd == "Recharge":
        amount = int(command[2])
        current_mp = heroes[hero]['mp'] + amount

        if current_mp > max_mp:
            regenerate = max_mp - heroes[hero]['mp']
            heroes[hero]['mp'] += regenerate
            print(f"{hero} recharged for {regenerate} MP!")
        else:
            print(f"{hero} recharged for {amount} MP!")
            heroes[hero]['mp'] += amount
    elif cmd == "Heal":
        amount = int(command[2])
        current_hp = heroes[hero]['hp'] + amount

        if current_hp > max_hp:
            regenerate = max_hp - heroes[hero]['hp']
            heroes[hero]['hp'] += regenerate
            print(f"{hero} healed for {regenerate} HP!")
        else:
            print(f"{hero} healed for {amount} HP!")
            heroes[hero]['hp'] += amount

    data = input()

for key, value in sorted(heroes.items(), key=lambda kvp: (-kvp[1]['hp'], kvp[0])):
    print(f"{key}\n  HP: {value['hp']}\n  MP: {value['mp']}")
