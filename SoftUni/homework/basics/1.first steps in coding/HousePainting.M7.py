#Зелена боя е за стените. Разхода за 1 литър 3.4 кв м
#Червена за покрива. Разхода -1 за 4.3 кв м

height_house = float(input())   #Височина на къщата
length_side_wall = float(input()) #Дължина на странична стена
height_triangle = float(input()) #Височина на триъгълна стена на покрива

side_area =  height_house * length_side_wall
window = 1.5 * 1.5
both_side1 = side_area * 2 - window * 2
back_wall = height_house * height_house
door = 1.2 * 2
both_side2 = back_wall * 2 - door
sum1 = both_side1 + both_side2
green_paint = sum1 / 3.4

print("{:.2f}".format(green_paint))

rectangle = 2 * (height_house * length_side_wall)
triangle = 2 * (height_house * height_triangle / 2)
sum2 = rectangle + triangle
red_paint = sum2 / 4.3

print("{:.2f}".format(red_paint))