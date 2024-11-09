"""
Module: vector.py
This is a simple implementation of a Vector class.
"""


class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self, d: int) -> None:
        """Create a `d`-dimensional vector of zeros.

        Args:
            - `d` (`int`): The dimension of the vector.
        """
        self._coords: list[int] = [0] * d

    def __len__(self) -> int:
        """Return the dimension of the vector.

        Returns:
            - `int`: The length of the vector.
        """
        return len(self._coords)

    def __getitem__(self, j: int) -> int:
        """Return the `j`-th coordinate of vector.

        Args:
            - `j` (`int`): The rank of the coordinate to find.

        Returns:
            - `int`: The coordinate of the vector.
        """
        return self._coords[j]

    def __setitem__(self, j: int, val: int) -> None:
        """Set the `j`-th coordinate of vector to a given value.

        Args:
            - `j` (`int`): The rank of the coordinate to set.
            - `val` (`int`): The value to set.
        """
        self._coords[j] = val

    def __add__(self, other: "Vector") -> "Vector":
        """Return the sum of two vectors.

        Args:
            - `other` (`Vector`): The other vector to add to the current instance.

        Raises:
            -  `NotImplementedError`: Raised when `other` is not a `Vector` object.

        Returns:
            - `Vector`: A new vector that is the sum of the 2 vector parameters.

        Assuming the two operands are vectors with the same length, this method creates
        a new vector and sets the coordinates of the new vector to be equal to the respective
        sum of the operands' elements.
        """
        if not isinstance(other, Vector):
            raise NotImplementedError("This functionality is not supported.")

        # Relies on len method
        if len(self) != len(other):
            raise ValueError("Dimensions must agree.")

        # Start with a vector of zeros
        result: Vector = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]

        return result

    def __eq__(self, other: object) -> bool:
        """Return `True` if the vector has the same coordinates as the other vector.

        Args:
            - `other` (`object`): The other object to check the equality to the current `Vector` instance.

        Raises:
            -  `NotImplementedError`: Raised when `other` is not a `Vector` object.

        Returns:
            - `bool`: Whether the current instance and the other object are equal.
        """
        if not isinstance(other, Vector):
            raise NotImplementedError("This functionality is not supported.")

        return self._coords == other._coords

    def __ne__(self, other: object) -> bool:
        """Return `True` if vector differs from other.

        Args:
            - `other` (`object`): The other object to check the non-equality to the current Vector instance.

        Raises:
            -  `NotImplementedError`: Raised when `other` is not a vector object.

        Returns:
            - `bool`: Whether the current instance and the other object are not equal.
        """
        if not isinstance(other, Vector):
            raise NotImplementedError("This functionality is not supported.")

        return not self == other  # Rely on existing __eq__ definition

    def __str__(self) -> str:
        """Produce string representation of vector.

        Returns:
            - `str`: The string representation of the vector.
        """
        # Adapt list representation
        return f"<{str(self._coords)[1:-1]}>"

    def __repr__(self) -> str:
        """Produce string representation of vector.

        Returns:
            - `str`: The string representation of the vector.
        """
        # Adapt list representation
        return f"<{str(self._coords)[1:-1]}>"


# Testing
if __name__ == "__main__":
    # Construct five-dimensional <0, 0, 0, 0, 0>
    vec: Vector = Vector(5)

    # <0, 23, 0, 0, 0> (based on use of __setitem__)
    vec[1] = 23

    # <0, 23, 0, 0, 45> (also via __setitem__)
    vec[-1] = 45

    print(f"{vec = }")
    print(f"{vec[4] = }")  # (via __getitem__)
