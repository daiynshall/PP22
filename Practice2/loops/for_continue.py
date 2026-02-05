# for_continue.py
# Practice 2: for + continue

numbers = [1, 2, 3, 4, 5, 6]

for x in numbers:
    if x % 2 == 0:
        # Skip even numbers
        continue
    print("Odd:", x)
