if __name__ == "__main__":
    # Example 1: sort numbers by absolute value
    nums = [3, -10, 1, -2, 7]
    by_abs = sorted(nums, key=lambda x: abs(x))
    print("by abs:", by_abs)

    # Example 2: sort tuples by second element
    pairs = [("a", 3), ("b", 1), ("c", 2)]
    by_second = sorted(pairs, key=lambda t: t[1])
    print("by second:", by_second)

    # Example 3: sort dicts by a field
    products = [
        {"name": "Mouse", "price": 12.5},
        {"name": "Keyboard", "price": 30.0},
        {"name": "Monitor", "price": 150.0},
    ]
    by_price = sorted(products, key=lambda p: p["price"])
    print("by price:", by_price)

    # Example 4: sort strings by last letter
    words = ["cat", "dog", "panda", "ant"]
    by_last_char = sorted(words, key=lambda w: w[-1])
    print("by last char:", by_last_char)
