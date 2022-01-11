from collections import deque


# Variant one
# class sequence_repeat:
#     def __init__(self, sequence, count):
#         self.sequence = sequence
#         self.count = count
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.count == 0:
#             raise StopIteration
#
#         char = self.sequence[self.index]
#         self.index += 1
#         if self.index >= len(self.sequence):
#             self.index = 0
#         self.count -= 1
#         return letter


# Variant two
# class sequence_repeat:
#     def __init__(self, sequence, number):
#         self.sequence = deque(sequence)
#         self.number = number
#         self.counter = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.counter == self.number:
#             raise StopIteration
#
#         char = self.sequence.popleft()
#         self.counter += 1
#         self.sequence.append(letter)
#         return letter

# Variant three
# class sequence_repeat:
#     def __init__(self, sequence, count):
#         self.sequence = sequence
#         self.count = count
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.count == 0:
#             raise StopIteration
#
#         char = self.sequence[self.index]
#         self.get_next_index()
#         self.count -= 1
#         return letter
#
#     def get_next_index(self):
#         self.index += 1
#         if self.index >= len(self.sequence):
#             self.index = 0


# Variant four
class sequence_repeat:
    def __init__(self, sequence, count):
        self.sequence = sequence
        self.count = count
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == 0:
            raise StopIteration

        char = self.sequence[self.index % len(self.sequence)]
        self.index += 1
        self.count -= 1
        return char


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')

