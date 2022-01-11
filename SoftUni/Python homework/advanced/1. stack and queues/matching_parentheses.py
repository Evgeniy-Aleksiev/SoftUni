text = input()
parentheses_index = []

for index, symbol in enumerate(text):
    if symbol == "(":
        parentheses_index.append(index)
    elif symbol == ")":
        start_index = parentheses_index.pop()
        print(text[start_index:index + 1])
