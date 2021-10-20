from collections import deque

def matching_gender(male, female):
    male_stack = [x for x in male if x > 0]
    female_queue = deque([x for x in female if x > 0])
    matches_cnt = 0

    while male_stack and female_queue:
        current_male = male_stack.pop()
        current_female = female_queue.popleft()

        if current_male % 25 == 0:
            if male_stack:
                male_stack.pop()
                female_queue.appendleft(current_female)
                continue
        if current_female % 25 == 0:
            if female_queue:
                female_queue.popleft()
                male_stack.append(current_male)
                continue

        if current_male == current_female:
            matches_cnt += 1
            continue

        current_male -= 2
        if current_male > 0:
            male_stack.append(current_male)

    return male_stack, female_queue, matches_cnt


male_sequence = [int(x) for x in input().split()]
female_sequence = [int(x) for x in input().split()]

male, female, matches_count = matching_gender(male_sequence, female_sequence)

print(f"Matches: {matches_count}")
if male:
    print(f'Males left: {", ".join(map(str, male[::-1]))}')
else:
    print("Males left: none")

if female:
    print(f'Females left: {", ".join(map(str, female))}')
else:
    print("Females left: none")
