class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.end = 0
        self.start = len(self.iterable) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            raise StopIteration

        current_iterable = self.iterable[self.start]
        self.start -= 1
        return current_iterable


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
