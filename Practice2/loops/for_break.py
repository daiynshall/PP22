# for_break.py
# Practice 2: for + break

numbers = [2, 4, 6, 8, 10, 12]
target = 8

for x in numbers:
    print("Checking", x)
    if x == target:
        print("Found target! Breaking.")
        break
