def repeat_string(count: int):
    return lambda a: a * count


string_input = input()
n = int(input())
repeat = repeat_string(n)
print(repeat(string_input))