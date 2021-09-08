people_cnt = int(input())
lifts_capacity = [int(num) for num in input().split()]

for index in range(len(lifts_capacity)):
    if people_cnt >= 4:
        if lifts_capacity[index] == 0:
            lifts_capacity[index] = 4
            people_cnt -= 4
        elif lifts_capacity[index] < 4:
            empty_spots = 4 - lifts_capacity[index]
            lifts_capacity[index] += empty_spots
            people_cnt -= empty_spots
    else:
        if lifts_capacity[index] == 0:
            lifts_capacity[index] += people_cnt
            people_cnt = 0
        elif lifts_capacity[index] < 4:
            empty_spots = 4 - lifts_capacity[index]
            lifts_capacity[index] += empty_spots
            people_cnt -= empty_spots
    if people_cnt == 0:
        break

str_lift_capacity = [str(i) for i in lifts_capacity]
cnt_full_capacity = lifts_capacity.count(4)

if people_cnt == 0 and not len(str_lift_capacity) == cnt_full_capacity:
    print(f"The lift has empty spots!\n{' '.join(str_lift_capacity)}")
elif not people_cnt == 0 and len(str_lift_capacity) == cnt_full_capacity:
    print(f"There isn't enough space! {people_cnt} people in a queue!\n{' '.join(str_lift_capacity)}")
elif people_cnt == 0 and len(str_lift_capacity) == cnt_full_capacity:
    print(' '.join(str_lift_capacity))
