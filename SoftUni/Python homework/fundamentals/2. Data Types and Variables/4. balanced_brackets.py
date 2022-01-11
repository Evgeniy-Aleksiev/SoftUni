n = int(input())

open_brackets_cnt = 0
closing_brackets_cnt = 0
balanced = True

for number_of_lines in range(n):
    text = input()

    if text == "(":
        open_brackets_cnt += 1
    elif text == ")":
        closing_brackets_cnt += 1

    if open_brackets_cnt - 1 > closing_brackets_cnt:
        balanced = False
        break
    if closing_brackets_cnt > open_brackets_cnt:
        balanced = False
        break

if balanced:
    print("BALANCED")
else:
    print("UNBALANCED")