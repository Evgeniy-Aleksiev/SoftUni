def list_manipulator(numbers, command, position, *args):
    if command == 'remove':
        if position == 'beginning':
            if args:
                return numbers[args[0]:]
            return numbers[1:]
        if position == 'end':
            if args:
                for x in args:
                    num = x
                    nums = numbers[::-1]
                    removed_num = nums[num:]
                    return removed_num[::-1]
            return numbers[:-1]

    if command == 'add':
        if position == 'beginning':
            for num in args[::-1]:
                numbers.insert(0, num)
            return numbers
        if position == 'end':
            numbers += args
            return numbers


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
