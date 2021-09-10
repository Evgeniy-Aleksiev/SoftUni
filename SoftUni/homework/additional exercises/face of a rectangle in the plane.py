x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())


# Ако извадим по-големият Х от по-малкият Х ще получим дължината на правоъгълника
# Ако извадим по-големият Y от по-малкият Y ще получим височината на правоъгълника
# За целта ще използваме функцията max() и min() за да намерим по-голямата и по-малката стойност

width = max(x1, x2) - min(x1, x2)
height = max(y1, y2) - min(y1, y2)
area = width * height
perimeter = 2 * (width + height)

print('Area = ', area)
print('Perimeter = ', perimeter)