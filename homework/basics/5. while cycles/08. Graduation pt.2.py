student_name = input()
current_class = 1
bad_tries = 0
grade = 0
its_rejected = False

while current_class <= 12:
    current_grade = float(input())
    if current_grade < 4:
        bad_tries += 1
        if bad_tries > 1:
            its_rejected = True
            break
        continue
    grade += current_grade
    current_class += 1
if its_rejected:
    print(f"{student_name} has been excluded at {current_class} grade")
else:
    average_grade = grade / 12
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")