# boolean_intro.py
# Practice 2: Boolean Values (W3Schools-inspired examples)
# Run: python boolean_intro.py

# In Python, booleans are True or False.
is_student = True
is_admin = False

print("is_student:", is_student)
print("is_admin:", is_admin)

# bool() converts values to True/False according to "truthiness"
print("bool(1):", bool(1))
print("bool(0):", bool(0))
print("bool('hello'):", bool("hello"))
print("bool(''):", bool(""))

# Any non-empty list is True, empty list is False
print("bool([1, 2, 3]):", bool([1, 2, 3]))
print("bool([]):", bool([]))
