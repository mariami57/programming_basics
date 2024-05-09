import math
import sys

n_easter_bread = int(input())

sugar_total_quantity = 0
flour_total_quantity = 0
max_sugar = -sys.maxsize
max_flour = -sys.maxsize

for easter_bread in range(n_easter_bread):
    sugar_gr = int(input())
    flour_gr = int(input())
    if sugar_gr > max_sugar:
        max_sugar = sugar_gr
    if flour_gr > max_flour:
        max_flour = flour_gr

    sugar_total_quantity += sugar_gr
    flour_total_quantity += flour_gr

sugar_packages = math.ceil(sugar_total_quantity / 950)
flour_packages = math.ceil(flour_total_quantity / 750)

print(f"Sugar: {sugar_packages}")
print(f"Flour: {flour_packages}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")



