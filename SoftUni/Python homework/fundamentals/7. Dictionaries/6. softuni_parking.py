n = int(input())

status = {}

for _ in range(1, n + 1):
    command = input().split()
    username = command[1]
    if command[0] == "register":
        register_number = command[2]
        if username not in status:
            status[username] = register_number
            print(f"{username} registered {register_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {status[username]}")
    elif command[0] == "unregister":
        if username not in status:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            status.pop(username)

for name, plate_number in status.items():
    print(f"{name} => {plate_number}")
