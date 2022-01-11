v = int(input()) # Обем на басейна в литри
p1 = int(input())  # Дебит на първата тръба за час
p2 = int(input())   # Дебит на втората тръба за час
h = float(input())  # Часове които работникът отсъства

p1 *= h
p2 *= h
total_liters = p1 + p2
percent_v = total_liters / v * 100
p1 = (p1 / total_liters) * 100
p2 = (p2 / total_liters) * 100

if total_liters > v:
    liters_more = total_liters - v
    print(f"For {h:.2f} hours the pool overflows with {liters_more} liters.")
else:
    print(f"The pool is {percent_v:.2f}% full. Pipe 1: {p1:.2f}%. Pipe 2: {p2:.2f}%.")