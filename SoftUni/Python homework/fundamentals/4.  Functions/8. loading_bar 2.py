def loading_bar(number: int):
    loading_points = number // 10
    percent_points = loading_points * "%"
    dot_points = (10 - loading_points) * "."

    if number == 100:
        print(f"100% Complete!\n[%%%%%%%%%%]")
    else:
        print(f"{number}% [{percent_points}{dot_points}]\nStill loading...")


num = int(input())
loading_bar(num)