number_of_jury = int(input())
number_of_presentations = 0
final_grade = 0
command = input()

while command != "Finish":
    current_presentation = command
    number_of_presentations += 1
    current_presentation_grade = 0
    for presentation_grade in range(number_of_jury):
        grade = float(input())
        current_presentation_grade += grade
    average_current_presentation = current_presentation_grade / number_of_jury
    final_grade += average_current_presentation
    print(f"{current_presentation} - {average_current_presentation:.2f}.")
    command = input()
average_final_grade = final_grade /  number_of_presentations
print(f"Student's final assessment is {average_final_grade:.2f}.")
