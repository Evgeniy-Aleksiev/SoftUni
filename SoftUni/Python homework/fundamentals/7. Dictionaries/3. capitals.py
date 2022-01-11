country = input().split(", ")
capital = input().split(", ")

zip_iterator = dict(zip(country, capital))
for key, value in zip_iterator.items():
    print(f"{key} -> {value}")
