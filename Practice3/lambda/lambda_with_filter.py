"""lambda + filter(): keep only elements that match a condition."""

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6]
    evens = list(filter(lambda x: x % 2 == 0, nums))
    print("evens =", evens)

    words = ["ai", "python", "ok", "code"]
    long_words = list(filter(lambda w: len(w) > 2, words))
    print("long_words =", long_words)
