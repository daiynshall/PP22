import math
import random

nums = [3, -8, 2, 10]

# 1) built-in
print("min:", min(nums))
print("max:", max(nums))
print("abs(-8):", abs(-8))
print("round(3.14159, 2):", round(3.14159, 2))
print("pow(2, 5):", pow(2, 5))

# 2) math module
print("sqrt(25):", math.sqrt(25))
print("ceil(2.1):", math.ceil(2.1))
print("floor(2.9):", math.floor(2.9))
print("pi:", math.pi)

# 3) random module
print("random():", random.random())        # 0..1
print("randint(1,6):", random.randint(1, 6))  # кубик
items = ["apple", "banana", "kiwi"]
print("choice:", random.choice(items))
random.shuffle(items)
print("shuffle:", items)
