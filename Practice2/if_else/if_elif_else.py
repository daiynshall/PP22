# if_elif_else.py
# Practice 2: If / Elif / Else + "switch-like" patterns

grade = 82

if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"

print("Grade:", grade, "Letter:", letter)

# "Switch-like" approach #1: dictionary mapping 
day = 3
day_name = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday",
}.get(day, "Unknown day")

print("Day:", day, "->", day_name)


