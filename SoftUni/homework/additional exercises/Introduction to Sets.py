def average(array):
    length = len(set(array))
    total_sum = sum(set(array))
    return total_sum / length


n = int(input())
arr = list(map(int, input().split()))
result = average(arr)
print(result)