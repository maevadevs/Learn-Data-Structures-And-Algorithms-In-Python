class Color:
    """A class representing a color"""

    def __init__(self, r: int, g: int, b: int) -> None:
        """Create a new instance of Color.

        Args:
            - `r (`int`): The value for the Red
            - `g` (`int`): The value for the Green
            - `b` (`int`): The value for the Blue
        """
        self._r: int = r
        self._g: int = g
        self._b: int = b

    def __str__(self) -> str:
        """Returns a string representing the color.

        Returns:
            - `str`: A string representing the color
        """
        return f"Color({self._r}, {self._g}, {self._b})"

    def __repr__(self) -> str:
        """Returns a string representing the color.

        Returns:
            - `str`: A string representing the color
        """
        return f"Color({self._r}, {self._g}, {self._b})"
