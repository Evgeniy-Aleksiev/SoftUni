nums = input().split()
rev_num_by_stack = []

for _ in range(len(nums)):
    rev_num_by_stack.append(nums.pop())

print(' '.join(rev_num_by_stack))



num = input().split()
num.reverse()
print(' '.join(num))