failed_threshold = int(input())
grades_sum = 0
poor_grades = 0
total_solved_tasks = 0
last_problem = " "
has_failed = True

# Задачата приключва команди при Enough или ако получи определен брой незадоволителни оценки


while poor_grades < failed_threshold:   # ако получи определен брой незадоволителни оценки
    problems_name = input()
    if problems_name == "Enough":  # ако получи команда Enough
        has_failed = False
        break
    grade = int(input())
    if grade <= 4:
        poor_grades += 1
    grades_sum += grade
    total_solved_tasks += 1
    last_problem = problems_name

if not has_failed:
    average_score = grades_sum / total_solved_tasks
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {total_solved_tasks}")
    print(f"Last problem: {last_problem}")
else:
    print(f"You need a break, {poor_grades} poor grades.")