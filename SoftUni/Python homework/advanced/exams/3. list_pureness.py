from collections import deque

def best_list_pureness(numbers, k):
    numbers_queue = deque(numbers)
    best_result = 0
    best_index = 0

    for index in range(k + 1):
        current_index_sum = sum([n * i for i, n in enumerate(numbers_queue)])
        if current_index_sum > best_result:
            best_index = index
            best_result = current_index_sum
        numbers_queue.appendleft(numbers_queue.pop())

    return f'Best pureness {best_result} after {best_index} rotations'

test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
