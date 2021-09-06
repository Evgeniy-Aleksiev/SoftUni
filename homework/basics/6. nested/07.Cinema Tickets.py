movie_name = input()
student_ticket = 0
standard_ticket = 0
kid_ticket = 0
total_ticket = 0

while movie_name != "Finish":
    free_seats = int(input())
    command = input()
    tickets = 0
    while command != "End":
        if free_seats > tickets:
            if command == "student":
                student_ticket += 1
            elif command == "standard":
                standard_ticket += 1
            elif command == "kid":
                kid_ticket += 1
            tickets += 1
            total_ticket += 1
        if free_seats == tickets:
            break
        command = input()
    filled_hall = tickets / free_seats * 100
    print(f"{movie_name} - {filled_hall:.2f}% full.")
    movie_name = input()
print(f"Total tickets: {total_ticket}")
students = student_ticket / total_ticket * 100
print(f"{students:.2f}% student tickets.")
standard = standard_ticket / total_ticket * 100
print(f"{standard:.2f}% standard tickets.")
kid = kid_ticket / total_ticket * 100
print(f"{kid:.2f}% kids tickets.")
