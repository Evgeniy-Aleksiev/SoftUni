income = float(input()) # Доход
average = float(input()) # Среден успех
salary = float(input()) # Минимална работна заплата

social_scholarship = int(salary * 0.35)
excellent = int(average * 25)
#1. Ако успеха на ученика е над 5.5 или равен
if average >= 5.5:
    #1.1 Ако не взима социална стипендия
    if income > salary:
        print(f"You get a scholarship for excellent results {excellent} BGN")
    #1.2 Ако взима социална стипендия
    else:
        #1.2.1 Ако социалната стипендия е по-висока
        if social_scholarship > excellent:
            print(f"You get a Social scholarship {social_scholarship} BGN")
        #1.2.1 Ако социалната стипендия е по-малка или равна
        else:
            print(f"You get a scholarship for excellent results {excellent} BGN")
#2. Ако успеха на ученика е над 4.5
elif average > 4.5:
    #2.1 Ако дохода на член от сем е по-малък от минималната заплата
    if income < salary:
        print(f"You get a Social scholarship {social_scholarship} BGN")
    #2.2 Ако дохода на член от сем е по-висок
    else:
        print("You cannot get a scholarship!")
#3. Ако успеха на ученика е под 3.5
else:
    print("You cannot get a scholarship!")
