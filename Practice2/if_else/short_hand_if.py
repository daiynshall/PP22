# short_hand_if.py
# Practice 2: Short hand if / else (ternary operator)

a = 5
b = 9

# Short-hand if (single line, single statement)
if a < b: print("a is smaller than b")

# Ternary (short-hand if-else)
result = "even" if b % 2 == 0 else "odd"
print("b is", result)

# Another ternary example
age = 17
status = "adult" if age >= 18 else "minor"
print("Age:", age, "Status:", status)
