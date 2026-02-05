# boolean_operators.py
# Practice 2: Boolean operators (and / or / not)

x = 5
y = 12

# and: True only if both are True
print("(x > 0) and (y > 0):", (x > 0) and (y > 0))
print("(x > 10) and (y > 0):", (x > 10) and (y > 0))

# or: True if at least one is True
print("(x > 10) or (y > 0):", (x > 10) or (y > 0))
print("(x > 10) or (y < 0):", (x > 10) or (y < 0))

# not: negates the boolean value
is_online = False
print("is_online:", is_online)
print("not is_online:", not is_online)

# Operator precedence example
# not has higher precedence than and/or, so use parentheses for clarity
a = True
b = False
c = True
print("a and not b:", a and (not b))
print("not (a and b):", not (a and b))
print("(a and b) or c:", (a and b) or c)
