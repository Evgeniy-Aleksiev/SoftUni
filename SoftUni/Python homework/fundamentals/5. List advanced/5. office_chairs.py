n = int(input())

chairs_left = 0
enough_chairs = True

for current_room in range(1, n + 1):
    chairs, visitors = input().split()

    if len(chairs) >= int(visitors):
        chairs_left += len(chairs) - int(visitors)

    else:
        need_chairs = int(visitors) - len(chairs)
        print(f"{need_chairs} more chairs needed in room {current_room}")
        enough_chairs = False

if enough_chairs:
    print(f"Game On, {chairs_left} free chairs left")
