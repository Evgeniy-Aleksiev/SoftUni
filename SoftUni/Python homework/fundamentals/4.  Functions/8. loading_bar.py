def integer_number_divisible_by_ten(number: int):
    percent_bars = 0
    if number % 10 == 0:
        percent_bars += number // 10
        return percent_bars


def loading_or_complete(number: int):
    if integer_number_divisible_by_ten(number) < 10:
        return False

    return True


def bars(number: int):
    current_number = integer_number_divisible_by_ten(number)
    percent_bars = current_number * "%"
    bars_list = percent_bars

    if current_number < 10:
        points = 10 - current_number
        bars_list += points * "."

    return bars_list


def loading_bar(number: int):
    if not loading_or_complete(number):
        print(f"{number}% [{bars(number)}]")
        print("Still loading...")
    else:
        print("100% Complete!")
        print(f"[{bars(number)}]")


num = int(input())
loading_bar(num)
