import math

degree = float(input("Enter the degree: "))
radian = math.radians(degree)

print(f"Output radian: {radian:.6f}")

#place 

height = float(input("Enter the height: "))
base1 = float(input("Enter the first base: "))
base2 = float(input("Enter the second base: "))

area = (base1 + base2) * height / 2
print("Area:", area)

#place

import math

n = int(input("Enter the number of sides: "))
m = float(input("Enter the length of a side: "))

area = (n * m ** 2) / (4 * math.tan(math.pi / n))
print("Area:", area)

#place 

import math

n = int(input("Enter the base:"))
m = int(input("Enter the length: "))

area = n * m
print("Area: ", area)