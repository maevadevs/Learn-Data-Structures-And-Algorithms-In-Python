"""
Module: progression.py
This is a simple implementation of Progression classes.
"""


# IMPLEMENT CLASS
# ---------------
class Progression:
    """Iterator producing a generic progression.

    Default iterator produces the whole numbers 0, 1, 2, ...
    """

    def __init__(self, start: int = 0) -> None:
        """Initialize `self._current` to the first value of the progression.

        Args:
            - `start` (`int`, optional): The number to start the progression at. Defaults to `0`.
        """
        self._current: int = start

    def _advance(self) -> None:
        """Update `self._current` to a new value.

        This should be overridden by a subclass to customize progression.
        By convention, if `self._current` is set to `None`, this designates the end of a finite progression.
        """
        self._current += 1

    def __next__(self) -> int:
        """Return the next element, or else raise `StopIteration` error.

        Raises:
            `StopIteration`: Raised when there are no more element and stops the iteration.

        Returns:
            - `int`: The next element in the iterator.
        """
        # Our convention to end a progression
        if self._current is None:
            raise StopIteration()
        else:
            # Record current value to return
            answer: int = self._current
            # Advance to prepare for next time
            self._advance()
            # Return the answer
            return answer

    def __iter__(self) -> "Progression":
        """By convention, an iterator must return itself as an iterator.

        Returns:
            - `Progression`: This progression instance.
        """
        return self

    def print_progression(self, n: int) -> None:
        """Print next `n` values of the progression.

        Args:
            - `n` (`int`): The next `n` values of the progression to print.
        """
        print(" ".join(str(next(self)) for _ in range(n)))


# IMPLEMENT CLASS
# ---------------
class ArithmeticProgression(Progression):
    """Iterator producing an arithmetic progression."""

    def __init__(self, increment: int = 1, start: int = 0) -> None:
        """Create a new arithmetic progression.

        Args:
            - `increment` (`int`, optional): The fixed constant to add to each term. Defaults to `1`.
            - `start` (`int`, optional): The first term of the progression. Defaults to `0`.
        """
        # Initialize base class
        super().__init__(start)
        self._increment: int = increment

    def _advance(self) -> None:  # Override inherited version
        """Update current value by adding the fixed increment."""
        self._current += self._increment


# IMPLEMENT CLASS
# ---------------
class GeometricProgression(Progression):
    """Iterator producing a geometric progression."""

    def __init__(self, base: int = 2, start: int = 1) -> None:
        """Create a new geometric progression.

        Args:
            - `base` (`int`, optional): The fixed constant multiplied to each term. Defaults to `2`.
            - `start` (`int`, optional): The first term of the progression. Defaults to `1`.
        """
        super().__init__(start)
        self._base: int = base

    def _advance(self) -> None:  # Override inherited version
        """Update current value by multiplying it by the base value."""
        self._current *= self._base


# IMPLEMENT CLASS
# ---------------
class FibonacciProgression(Progression):
    """Iterator producing a generalized Fibonacci progression."""

    def __init__(self, first: int = 0, second: int = 1) -> None:
        """Create a new fibonacci progression.

        Args:
            - `first` (`int`, optional): The first term of the progression. Defaults to `0`.
            - `second` (`int`, optional): The second term of the progression. Defaults to `1`.
        """
        # Start progression at first
        super().__init__(first)
        # Fictitious value preceding the first
        self._prev: int = second - first

    def _advance(self) -> None:
        """Update current value by taking sum of previous two."""
        self._prev, self._current = self._current, self._prev + self._current


# UNIT TESTS
# ----------
if __name__ == "__main__":
    print("Default progression:")
    Progression().print_progression(10)

    print("Arithmetic progression with increment 5:")
    ArithmeticProgression(5).print_progression(10)

    print("Arithmetic progression with increment 5 and start 2:")
    ArithmeticProgression(5, 2).print_progression(10)

    print("Geometric progression with default base:")
    GeometricProgression().print_progression(10)

    print("Geometric progression with base 3:")
    GeometricProgression(3).print_progression(10)

    print("Fibonacci progression with default start values:")
    FibonacciProgression().print_progression(10)

    print("Fibonacci progression with start values 4 and 6:")
    FibonacciProgression(4, 6).print_progression(10)
