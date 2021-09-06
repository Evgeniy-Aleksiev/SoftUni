command = input()
prime_numbers = 0
non_prime_numbers = 0
while command != "stop":
    number = int(command)
    is_prime = True
    if number < 0:
        print("Number is negative.")
        command = input()
        continue
    for current_number in range(2, number):
        if number % current_number == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers += number
    else:
        non_prime_numbers += number
    command = input()
print(f"Sum of all prime numbers is: {prime_numbers}")
print(f"Sum of all non prime numbers is: {non_prime_numbers}")

