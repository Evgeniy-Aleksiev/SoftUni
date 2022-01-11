# Желан резултат
# Започва тренировката 30см по-ниско от целта
# За всяка височина има право на 3 скока, като за да бъде успешен трябва да бъде над височината на летвата
# При успешен скок, височината се вдига с 5см
# Тренировката приключва при 3 неуспешни скока на една и съща височина или при достигане на желаната височина

target_height = int(input())
stick_height = target_height - 30
total_jumps = 0
failed = False
while stick_height <= target_height:
    bad_jumps = 0
    for jumps in range(1, 4):
        total_jumps += 1
        height_jump = int(input())
        if height_jump > stick_height:
            stick_height += 5
            break
        else:
            bad_jumps += 1
    if bad_jumps == 3:
        failed = True
        break
if failed:
    print(f"Tihomir failed at {stick_height}cm after {total_jumps} jumps.")
else:
    print(f"Tihomir succeeded, he jumped over {target_height}cm after {total_jumps} jumps.")