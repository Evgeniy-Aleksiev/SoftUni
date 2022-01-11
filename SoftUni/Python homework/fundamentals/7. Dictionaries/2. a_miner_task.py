resource = input()

miner_task = {}

while not resource == "stop":
    quantity = int(input())
    if resource not in miner_task:
        miner_task[resource] = 0
    miner_task[resource] += quantity

    resource = input()

for key, value in miner_task.items():
    print(f"{key} -> {value}")
