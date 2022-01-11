from string import ascii_lowercase as chars


def print_rangoli(size):
    heap = [('-'.join(chars[i:size])[::-1] + '-'.join(chars[i:size])[1:]).center(4 * n - 3, '-') for i in range(size)]
    print(*(heap[::-1] + heap[1:]), sep="\n")


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
