import sys
from math import ceil

eastern_bread_number = int(input())

total_sugar_grams = 0
total_flour_grams = 0
max_sugar_grams = -sys.maxsize
max_flour_grams = -sys.maxsize

for eastern_bread in range(eastern_bread_number):
    sugar = int(input())
    flour = int(input())
    total_sugar_grams += sugar
    total_flour_grams += flour
    if sugar > max_sugar_grams:
        max_sugar_grams = sugar
    if flour > max_flour_grams:
        max_flour_grams = flour

package_sugar = ceil(total_sugar_grams / 950)
package_flour = ceil(total_flour_grams / 750)

print(f"Sugar: {package_sugar}")
print(f"Flour: {package_flour}")
print(f"Max used flour is {max_flour_grams} grams, max used sugar is {max_sugar_grams} grams.")
