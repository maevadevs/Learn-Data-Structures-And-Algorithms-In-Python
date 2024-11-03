# IMPORT MODULES
# --------------
from typing import Iterable, TypeVar, Generator

# CUSTOM TYPES
# ------------
TCount = TypeVar("TCount", str, int, float, bool)
TNumeric = TypeVar("TNumeric", int, float)


# Example of a function
# ---------------------
def count(target: TCount, data: Iterable[TCount]) -> int:
    """Counts the number of occurrences of a given `target` value within any form of iterable `data` set.

    Args:
        - `target` (`TypeVar("TCount", str, int, float, bool)`): The target value.
        - `data` (`Iterable[TCount]`): The iterable set.

    Returns:
        - `int`: The number of occurences of `target` within `data`

    The `target` can be any value of type `str`, `int`, `float`, or `bool`.
    """

    # The count of occurences
    cnt: int = 0

    # Loop through the items in the data
    for item in data:
        if item == target:
            cnt += 1

    # Return count of occurences
    return cnt


def contains(target: str, data: str) -> bool:
    """Checks whether a `target` string is contained in another `data` string or not.

    Args:
        - `target` (`str`): The string to check if being contained.
        - `data` (`str`): The string to check into if it contains the `target` string.

    Returns:
        - `bool`: Whether the `target` string is contained in `data` or not.
    """

    for item in data:
        if item == target:
            # If here, the item was found
            return True

    # If here, then not found
    return False


def scale(data: list[TNumeric], factor: TNumeric) -> None:
    """Multiply all entries of a numeric `data` set by a given `factor`.

    Args:
        - `data` (`list[TNumeric]`): A list of numeric data to multiply.
        - `factor` (`TNumeric`): The factor to multiply by.
    """

    for j in range(len(data)):
        data[j] *= factor


def factors_func(n: int) -> list[int]:
    """A traditional function that computes factors.

    Args:
        - `n` (`int`): The integer that we want to compute the factors of.

    Returns:
        - `list[int]`: The factors of the given number.
    """

    # Store factors in a new list
    factors: list[int] = []

    for k in range(1, n + 1):
        if n % k == 0:  # Divides evenly, thus k is a factor
            # Add k to the list of factors
            factors.append(k)

    # Return the entire list
    return factors


# List of factors for a given integer
def factors_func_2(n: int) -> list[int]:
    """A traditional function that computes factors.

    Args:
        - `n` (`int`): The integer that we want to compute the factors of.

    Returns:
        - `list[int]`: The factors of the given number.
    """

    return [k for k in range(1, n + 1) if n % k == 0]


def factors_gen(n: int) -> Generator[int, None, None]:
    """A generator that computes factors.

    Args:
        - `n` (`int`): The integer that we want to compute the factors of.

    Yields:
        - `Generator[int, None, None]`: Generator of the factors of `n`.
    """

    for k in range(1, n + 1):
        if n % k == 0:  # Divides evenly, thus k is a factor
            # Yield this factor as next result
            yield k


def factors_gen_2(n: int) -> Generator[int, None, None]:
    """A generator that computes factors.

    Args:
        - `n` (`int`): The integer that we want to compute the factors of.

    Yields:
        - `Generator[int, None, None]`: Generator of the factors of `n`.
    """

    # Declare and initialize variables
    k: int = 1

    while k * k < n:  # While k < sqrt(n)
        if n % k == 0:
            yield k
            yield n // k
        k += 1

    if k * k == n:  # Special case if n is perfect square
        yield k


def fibonacci_gen() -> Generator[int, None, None]:
    """A generator of fibonaci sequence.

    Yields:
        - `Generator[int, None, None]`: The sequence of Fibonacci numbers.
    """

    # Declare and initialize variables
    a: int = 0
    b: int = 1

    while True:  # keep going...
        yield a  # report value, a, during this pass
        future = a + b
        a = b  # this will be next value reported
        b = future  # and subsequently this


def fibonacci_gen_2() -> Generator[int, None, None]:
    """A generator of fibonaci sequence.

    Yields:
        - `Generator[int, None, None]`: The sequence of Fibonacci numbers.
    """
    # Declare variables
    a: int
    b: int

    # Initialize variable
    a, b = 0, 1

    while True:  # keep going...
        yield a  # report value, a, during this pass
        a, b = b, a + b
