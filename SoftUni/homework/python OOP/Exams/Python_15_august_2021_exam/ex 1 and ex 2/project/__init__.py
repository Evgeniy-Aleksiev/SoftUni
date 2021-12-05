from project.baked_food.bread import Bread
from project.bakery import  Bakery


b = Bakery('Pesho')

b.add_food('Bread', 'Topal', 2)
b.add_food('Bread', 'Pitka', 2.50)
b.add_food('Cake', 'Hubava', 6)

b.add_drink('Tea', 'Angliiski', 3, 'brand 1')
b.add_drink('Water', 'Mineralna', 1, 'Was')

b.add_table('InsideTable', 15, 10)
b.add_table('OutsideTable', 52, 10)

#print(b.get_free_tables_info())
print(b.reserve_table(15))
print(b.order_food(15, 'Mineralna', 'Mineralna', 'Mineralna', 'Topla', 'Hubava'))
print(b.order_drink(15, 'Mineralna', 'Mineralna', 'Mineralna', 'Topla', 'Hubava'))