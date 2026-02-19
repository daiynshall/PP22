if __name__ == "__main__":
    # Example 1: basic lambda (like a tiny function)
    double = lambda x: x * 2
    print("double(8) =", double(8))

    # Example 2: lambda with two arguments
    add = lambda a, b: a + b
    print("add(3, 9) =", add(3, 9))

    # Example 3: immediate use (IIFE style)
    print("immediate result:", (lambda x: x ** 2 + 1)(5))

    # Example 4: lambda as a key function (preview; sorted used more in other file)
    words = ["banana", "kiwi", "strawberry", "fig"]
    by_length = sorted(words, key=lambda w: len(w))
    print("sorted by length:", by_length)
