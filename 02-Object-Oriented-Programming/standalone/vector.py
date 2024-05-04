"""
Module: vector.py
This is a simple implementation of a Vector class.
"""


class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self, d: int) -> None:
        """Create a d-dimensional vector of zeros.

        Args:
            - `d` (`int`): The dimension of the vector
        """
        self._coords: list[int] = [0] * d

    def __len__(self) -> int:
        """Return the dimension of the vector.

        Returns:
            - `int`: The length of the vector
        """
        return len(self._coords)

    def __getitem__(self, j: int) -> int:
        """Return the jth coordinate of vector.

        Args:
            - `j` (`int`): The rank of the coordinate to find

        Returns:
            - `int`: The coordinate of the vector
        """
        return self._coords[j]

    def __setitem__(self, j: int, val: int) -> None:
        """Set the jth coordinate of vector to a given value.

        Args:
            - `j` (`int`): The rank of the coordinate to set
            - `val` (`int`): The value to set
        """
        self._coords[j] = val

    def __add__(self, other: "Vector") -> "Vector":
        """Return the sum of two vectors.

        Args:
            - `other` (`Vector`): The other vector to add to the current instance

        Returns:
            - `Vector`: A new vector that is the sum of the 2 vector parameters

        Assuming the two operands are vectors with the same length, this method creates
        a new vector and sets the coordinates of the new vector to be equal to the respective
        sum of the operands' elements.
        """
        if len(self) != len(other):  # relies on len method
            raise ValueError("Dimensions must agree")

        result: Vector = Vector(len(self))  # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]

        return result

    def __eq__(self, other: object) -> bool:
        """Return True if the vector has the same coordinates as the other vector.

        Args:
            - `other` (`object`): The other object to check the equality to the current Vector instance

        Raises:
            -  `NotImplementedError`: Raised when `other` is not a vector object.

        Returns:
            - `bool`: Whether the current instance and the other object are equal
        """
        if not isinstance(other, Vector):
            raise NotImplementedError("This functionality is not supported")

        return self._coords == other._coords

    def __ne__(self, other: object) -> bool:
        """Return True if vector differs from other.

        Args:
            - `other` (`object`): The other object to check the non-equality to the current Vector instance

        Raises:
            -  `NotImplementedError`: Raised when `other` is not a vector object.

        Returns:
            - `bool`: Whether the current instance and the other object are not equal
        """
        if not isinstance(other, Vector):
            raise NotImplementedError("This functionality is not supported")

        return not self == other  # rely on existing eq definition

    def __str__(self) -> str:
        """Produce string representation of vector.

        Returns:
            - `str`: The string representation of the vector
        """
        return f"<{str(self._coords)[1:-1]}>"  # adapt list representation


# Testing
if __name__ == "__main__":
    v: Vector = Vector(5)  # construct five-dimensional <0, 0, 0, 0, 0>

    v[1] = 23  # <0, 23, 0, 0, 0> (based on use of __setitem__)
    v[-1] = 45  # <0, 23, 0, 0, 45> (also via __setitem__)
    print(v[4])  # print 45 (via __getitem__)

    u: Vector = v + v  # <0, 46, 0, 0, 90> (via __add__)
    print(u)  # print <0, 46, 0, 0, 90>
