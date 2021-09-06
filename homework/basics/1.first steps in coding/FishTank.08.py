length = int(input())
width = int(input())
height = int(input())
volume = float(input())

aqua_volume = length * width * height
liters = aqua_volume * 0.001
percent = volume / 100
liters_need = liters * (1 - percent)

print(liters_need)