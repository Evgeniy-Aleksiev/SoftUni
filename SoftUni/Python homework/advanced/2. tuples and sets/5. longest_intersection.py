longest_intersection = []

for _ in range(int(input())):
    first, second = input().split('-')
    first_start, first_end = [int(x) for x in first.split(',')]
    second_start, second_end = [int(x) for x in second.split(',')]
    first_range = set(range(first_start, first_end + 1))
    second_range = set(range(second_start, second_end + 1))

    intersection = first_range.intersection(second_range)
    if len(longest_intersection) < len(intersection):
        longest_intersection = list(intersection)

print(f"Longest intersection is {longest_intersection} with length {len(longest_intersection)}")