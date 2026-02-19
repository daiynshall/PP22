def greet(name: str) -> str:
    """Return a friendly greeting for the given name."""
    return f"Hello, {name}!"


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def is_even(n: int) -> bool:
    """Return True if n is even, otherwise False."""
    return n % 2 == 0


def factorial(n: int) -> int:
    """Compute n! (factorial) using a loop."""
    if n < 0:
        raise ValueError("n must be >= 0")
    result = 1
    for k in range(2, n + 1):
        result *= k
    return result


if __name__ == "__main__":
    # Example 1: simple call
    print(greet("Aruzhan"))

    # Example 2: function returning a number
    print("add(3, 7) =", add(3, 7))

    # Example 3: boolean return
    print("is_even(10) =", is_even(10))
    print("is_even(11) =", is_even(11))

    # Example 4: factorial with validation
    print("factorial(5) =", factorial(5))
