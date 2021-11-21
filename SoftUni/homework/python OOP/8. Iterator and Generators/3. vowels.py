class vowels:
    def __init__(self, text):
        self.text = text
        self.vowels = 'AEIOUYaeiouy'
        self.all_vowels = [x for x in self.text if x in self.vowels]
        self.start = 0
        self.end = len(self.all_vowels) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration

        index = self.start
        self.start += 1
        return self.all_vowels[index]


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
