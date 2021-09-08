def its_valid(index: int):
    if 0 <= index < len(target_value):
        return True
    return False


def shoot(index: int):
    if its_valid(index):
        for current_target in range(len(target_value)):
            if not target_value[current_target] == -1 and not index == current_target:
                if target_value[index] < target_value[current_target]:
                    target_value[current_target] -= target_value[index]
                else:
                    target_value[current_target] += target_value[index]
        target_value[index] = -1


target_value = [int(x) for x in (input()).split()]
command = input()

while not command == "End":
    shoot_index = int(command)
    shoot(shoot_index)
    command = input()

count_of_shoot_targets = target_value.count(-1)
targets = [str(x) for x in target_value]
print(f"Shot targets: {count_of_shoot_targets} -> {' '.join(targets)}")
