"""
Module: range.py
This is a simple implementation of a Range class.
"""

# IMPORT MODULES
# --------------
from typing import Optional


# IMPLEMENT CLASS
# ---------------
class Range:
    """A class that mimics the built-in range class."""

    def __init__(self, start: int, stop: Optional[int] = None, step: int = 1) -> None:
        """Initialize a Range instance.

        Args:
            - `start` (`int`): The starting point of the range.
            - `stop` (`Optional[int]`, optional): The stopping point of the range. Defaults to `None`.
            - `step` (`int`, optional): The step of the range. Defaults to `1`.

        Raises:
            - `ValueError`: Raised if the `step` is set to `0`

        Semantics is similar to built-in `range` class.
        """
        if step == 0:
            raise ValueError("step cannot be 0.")

        # Special case of range(n)
        if stop is None:
            # Should be treated as if range(0,n)
            start, stop = 0, start

        # Calculate the effective length once
        self._length: int = max(0, (stop - start + step - 1) // step)

        # Need knowledge of start and step (but not stop) to support getitem
        self._start: int = start
        self._step: int = step

    def __len__(self) -> int:
        """Return number of entries in the range.

        Returns:
            - `int`: The number of entries in the range.
        """
        return self._length

    def __getitem__(self, k: int) -> int:
        """Return entry at index `k` (using standard interpretation if negative).

        Args:
            - `k` (`int`): The index that we want to get the item of.

        Raises:
            - `IndexError`: Raised when `k < 0` or `k > self._length`.

        Returns:
            - `int`: The entry at the given index.
        """
        if k < 0:
            # Attempt to convert negative index
            k += len(self)

        if not 0 <= k < self._length:
            raise IndexError("index out of range.")

        return self._start + k * self._step
