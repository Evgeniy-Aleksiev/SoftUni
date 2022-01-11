def char_log_range(password: str):
    if 6 <= len(password) <= 10:
        return True

    return False


def check_for_letters_or_digits(password: str):
    if password.isalnum():
        return True
    else:
        return False


def at_least_two_digits(password: str):
    digit_count = 0

    for current_str in range(len(password)):
        if password[current_str].isdigit():
            digit_count += 1

    if digit_count >= 2:
        return True
    else:
        return False


def validation(password):
    valid = True
    if not char_log_range(password):
        print("Password must be between 6 and 10 characters")
        valid = False

    if not check_for_letters_or_digits(password):
        print("Password must consist only of letters and digits")
        valid = False

    if not at_least_two_digits(password):
        print("Password must have at least 2 digits")
        valid = False

    if valid:
        print("Password is valid")


password_input = input()
validation(password_input)