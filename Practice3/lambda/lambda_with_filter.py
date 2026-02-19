if __name__ == "__main__":
    # Example 1: keep only even numbers
    nums = list(range(1, 16))
    evens = list(filter(lambda x: x % 2 == 0, nums))
    print("evens:", evens)

    # Example 2: keep only positive numbers
    mixed = [-3, -1, 0, 2, 7, -10, 5]
    positives = list(filter(lambda x: x > 0, mixed))
    print("positives:", positives)

    # Example 3: keep long words
    words = ["hi", "computer", "ok", "python", "ai"]
    long_words = list(filter(lambda w: len(w) >= 4, words))
    print("long words:", long_words)

    # Example 4: filter dict items (students with GPA >= 3.5)
    students = [{"name": "Ali", "gpa": 3.2}, {"name": "Dana", "gpa": 3.8}, {"name": "Samat", "gpa": 3.6}]
    strong = list(filter(lambda st: st["gpa"] >= 3.5, students))
    print("strong students:", strong)
