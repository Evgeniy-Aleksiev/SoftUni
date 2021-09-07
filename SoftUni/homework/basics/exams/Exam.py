students_number = int(input())

top_students = 0
very_good_students = 0
good = 0
fail = 0
average = 0
for student in range(students_number):
    evaluation = float(input())
    average += evaluation
    if evaluation >= 5:
        top_students += 1
    elif 4 <= evaluation < 5:
        very_good_students += 1
    elif 3 <= evaluation < 4:
        good += 1
    else:
        fail += 1

average_top_students = top_students / students_number * 100
print(f"Top students: {average_top_students:.2f}%")
average_very_good_students = very_good_students / students_number * 100
print(f"Between 4.00 and 4.99: {average_very_good_students:.2f}%")
average_good = good / students_number * 100
print(f"Between 3.00 and 3.99: {average_good:.2f}%")
average_fail = fail / students_number * 100
print(f"Fail: {average_fail:.2f}%")
average_exam = average / students_number
print(f"Average: {average_exam:.2f}")