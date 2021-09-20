from collections import deque

expression = input()
parentheses = deque()
is_balanced = True
balanced = {
    '(': ')',
    '{': '}',
    '[': ']'
}

for el in expression:

    if el in '({[':
        parentheses.append(el)
    else:
        if not parentheses:
            is_balanced = False
            break
        last_bracket = parentheses.pop()
        if not balanced[last_bracket] == el:
            is_balanced = False
            break

if is_balanced and not parentheses:
    print("YES")
else:
    print("NO")