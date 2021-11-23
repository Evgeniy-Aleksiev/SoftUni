ll = [1, 2, 3, 4]

iter1 = iter(ll)
iter2 = iter(ll)

print('From iter1: ', next(iter1))

print('From iter2: ', next(iter2))

print('From iter1: ', next(iter1))
print('From iter1: ', next(iter1))

print('\n----------\n')

iter_obj = iter([1, 2, 3, 4])
while True:
    try:
        print(next(iter_obj))
    except StopIteration:
        print('Stop iteration')
        break
