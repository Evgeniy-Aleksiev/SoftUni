text = input()
counts = {}

for ch in text:
    if ch not in counts:
        counts[ch] = 0
    counts[ch] += 1

for key, value in sorted(counts.items()):
    print(f"{key}: {value} time/s")
