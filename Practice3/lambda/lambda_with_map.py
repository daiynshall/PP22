if __name__ == "__main__":
    # Example 1: square numbers
    nums = [1, 2, 3, 4, 5]
    squares = list(map(lambda x: x * x, nums))
    print("squares:", squares)

    # Example 2: convert strings to uppercase
    names = ["aigerim", "daniyar", "serik"]
    upper_names = list(map(lambda s: s.upper(), names))
    print("upper:", upper_names)

    # Example 3: extract field from list of dicts
    students = [{"name": "Ali", "gpa": 3.2}, {"name": "Dana", "gpa": 3.8}]
    gpas = list(map(lambda st: st["gpa"], students))
    print("gpas:", gpas)

    # Example 4: apply rounding to floats
    prices = [10.123, 5.5555, 99.999]
    rounded = list(map(lambda p: round(p, 2), prices))
    print("rounded:", rounded)
