data = input()

force_book = {}

while not data == "Lumpawaroo":
    not_in_force_book = True
    if "|" in data:
        force_side, force_user = data.split(" | ")
        for user_list in force_book.values():
            if force_user in user_list:
                not_in_force_book = False
        if force_side not in force_book and not_in_force_book:
            force_book[force_side] = []
            force_book[force_side].append(force_user)
        elif force_side in force_book and not_in_force_book:
            force_book[force_side].append(force_user)

    elif "->" in data:
        user_force, side_force = data.split(" -> ")
        for side, users in force_book.items():
            if user_force in users:
                not_in_force_book = False
                force_book[side].remove(user_force)
                force_book[side_force].append(user_force)

        if side_force not in force_book and not_in_force_book:
            force_book[side_force] = []
            force_book[side_force].append(user_force)
        elif not_in_force_book:
            force_book[side_force].append(user_force)
        print(f"{user_force} joins the {side_force} side!")

    data = input()

for key, value in sorted(force_book.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])):
    if len(value) > 0:
        print(f"Side: {key}, Members: {len(value)}")
        [print(f"! {user}") for user in sorted(value)]

