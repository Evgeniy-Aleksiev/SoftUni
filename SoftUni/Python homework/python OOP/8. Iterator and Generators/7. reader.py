def read_next(*args):
    for iterator in args:
        for ch in iterator:
            yield ch

for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)
