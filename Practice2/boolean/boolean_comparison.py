# boolean_comparison.py
# Practice 2: Booleans as comparison results

a = 10
b = 7
c = 10

print("a > b:", a > b)      # True
print("a < b:", a < b)      # False
print("a == c:", a == c)    # True
print("a != c:", a != c)    # False

name = "Aida"
print("name == 'Aida':", name == "Aida")
print("name == 'aida':", name == "aida")  # case-sensitive

# Comparing strings is lexicographical (dictionary-like) by Unicode code points
print("'ab' < 'cd':", "ab" < "cd")
print("'Z' < 'a':", "Z" < "a")
