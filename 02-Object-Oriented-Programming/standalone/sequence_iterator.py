"""
Module: sequence_iterator.py
This is a simple implementation of a SequenceIterator class.
"""

# IMPORT MODULES
# --------------
from typing import Any, Sequence


# IMPLEMENT CLASS
# ---------------
class SequenceIterator:
    """An iterator for any of Python's sequence types."""

    def __init__(self, sequence: Sequence[Any]) -> None:
        """Create an iterator for the given sequence.

        Args:
            - `sequence` (`Sequence[Any]`): The sequence to create an iterator for.
        """
        # Keep a reference to the underlying data
        self._seq: Sequence[Any] = sequence
        # Will increment to 0 on first call to next
        self._k: int = -1

    def __next__(self) -> Any:
        """Return the next element, or else raise `StopIteration` error.

        Raises:
            - `StopIteration`: Raised when there are no more elements in the iterator.

        Returns:
            - `Any`: The element from the iterator.
        """
        # Advance to next index
        self._k += 1

        if self._k < len(self._seq):
            # Return the data element
            return self._seq[self._k]
        else:
            # There are no more elements
            raise StopIteration()

    def __iter__(self) -> "SequenceIterator":
        """By convention, an iterator must return itself as an iterator.

        Returns:
            - `SequenceIterator`: The iterator instance.
        """
        return self
