from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque(map(int, input().split()))
intelligence_value = int(input())

shot = gun_barrel_size

while bullets and locks:
    bullet_size = bullets.pop()
    current_lock = locks[0]
    intelligence_value -= bullet_price
    shot -= 1

    if bullet_size <= current_lock:
        print("Bang!")
        locks.popleft()
    else:
        print("Ping!")

    if shot == 0 and bullets:
        print("Reloading!")
        shot = gun_barrel_size

if not locks:
    print(f"{len(bullets)} bullets left. Earned ${intelligence_value}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")


