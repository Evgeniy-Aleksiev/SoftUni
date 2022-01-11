n = int(input())
salary = int(input())
still_have_salary = True
for browser in range(1, n + 1):
    browser = input()
    if browser == "Facebook":
        salary -= 150
    elif browser == "Instagram":
        salary -= 100
    elif browser == "Reddit":
        salary -= 50
    if salary <= 0:
        still_have_salary = False
        print("You have lost your salary.")
        break

if still_have_salary:
    print(salary)
