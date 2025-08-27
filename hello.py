# hello.py


def say_hello(name: str) -> str:
    """Return a personalized greeting."""
    return (
        f"Hello, {name}! This is Eric Ortega, your TA for Data Engineering "
        "Systems (IDS 706)."
    )


def add(a: int, b: int) -> int:
    """Return the sum of two numbers."""
    return a + b


if __name__ == "__main__":
    # Demo run
    print(say_hello("students"))
    print("2 + 3 =", add(2, 3))
