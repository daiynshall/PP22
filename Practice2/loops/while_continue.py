# while_continue.py
# Practice 2: while + continue

i = 0
while i < 6:
    i += 1
    if i == 3:
        # skip printing 3
        continue
    print("i =", i)
