students_count = int(input())
lectures = int(input())
additional_bonus = int(input())

max_bonus = 0
max_attendances = 0

if lectures > 0:
    for current_student in range(1, students_count + 1):
        attendances_count = int(input())
        total_bonus = round(attendances_count / lectures * (5 + additional_bonus))
        if total_bonus > max_bonus:
            max_bonus = total_bonus
            max_attendances = attendances_count

print(f"Max Bonus: {max_bonus}.\nThe student has attended {max_attendances} lectures.")
