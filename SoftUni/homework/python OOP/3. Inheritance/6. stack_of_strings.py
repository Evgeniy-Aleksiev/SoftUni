class Stack(list):
    def  __init__(self):
        super().__init__()
        self.data = []

    def push(self, element):
        self.data.append(str(element))

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        return f"[{', '.join(self.data[::-1])}]"


a = Stack()
print(a.is_empty())
a.push(123)
a.push('Evgeniy')
a.push('Petar')
a.push('Ema')
print(a)
print(a.pop())
print(a.top())
print(a.is_empty())
print(a)
