def min_max(values: list[int]) -> tuple[int, int]:
    """Return (min, max) of a list."""
    if not values:
        raise ValueError("values list must not be empty")
    return min(values), max(values)


def grade(score: int) -> str:
    """Early return example."""
    if score < 0 or score > 100:
        return "Invalid"
    if score >= 90:
        return "A"
    if score >= 75:
        return "B"
    if score >= 60:
        return "C"
    return "F"


def make_multiplier(factor: int):
    """
    Return a function (closure) that multiplies by 'factor'.
    This is a great example of functions as objects.
    """
    def multiply(x: int) -> int:
        return x * factor

    return multiply


if __name__ == "__main__":
    # Example 1: tuple return
    nums = [10, 3, 99, 7, 42]
    mn, mx = min_max(nums)
    print("min =", mn, "max =", mx)

    # Example 2: early returns
    for s in [101, 95, 80, 62, 40]:
        print(s, "->", grade(s))

    # Example 3: returning a function
    times3 = make_multiplier(3)
    print("times3(14) =", times3(14))

    # Example 4: another multiplier
    times10 = make_multiplier(10)
    print("times10(6) =", times10(6))
