#!/usr/bin/env python
# coding: utf-8


def scale_short(data: list[int], factor: int) -> None:
    """Multiply all entries of numeric data list by the given factor."""

    # data is a list of integer that is passed by reference
    for j in range(len(data)):
        data[j] *= factor


def scale_complete(data: list[int], factor: int) -> None:
    """Multiply all entries of numeric data list by the given factor.

    Args:
        - `data` (`list[int]`): The list of integers to scale.
        - `factor` (`int`): The multiplicative factor by which we want to scale the data.

    Returns: `None`

    Raises: `None`

    This is a very simple implementation of a scaling function for demo-purposes.
    In a real-world scenario, we may want to add much more additional features to this function.

    As the function is currently written, it will accept any Sequence-type of integer for the `data`, such as a string of integers.

    `data` is a list of integer that is passed to the function by reference.
    Thus, we apply the transformation on this object directly and there is nothing to return from the function.

    Note that we are currently not doing any error-checking on this function. If we did, the Raises section would have some value.
    """

    # `data` is a list of integer that is passed by reference
    # Thus, we don't need to return anything
    for j in range(len(data)):
        data[j] *= factor


from decimal import Decimal

"""
Module: credit_card.py
This is a simple implementation of a CreditCard class. We use Decimal for all numbers.
"""


class CreditCard:
    """A consumer credit card class."""

    def __init__(
        self,
        customer: str,
        bank: str,
        account: str,
        limit: Decimal,
        starting_balance: Decimal = Decimal(0),
    ) -> None:
        """Create a new credit card instance with zero initial balance (default).

        Args:
            - `customer` (`string`): The name of the customer.
            - `bank` (`string`): The name of the bank.
            - `account` (`string`): The account identifier.
            - `limit` (`Decimal`): The credit limit.
            - `starting_balance` (`Decimal`): The starting balance of the account.

        Returns:
            - `None`
        """
        self._customer: str = customer
        self._bank: str = bank
        self._account: str = account
        self._limit: Decimal = limit
        self._balance: Decimal = starting_balance

    def get_customer(self) -> str:
        """Return the name of the customer on the credit card.

        Args:
            - `None`

        Returns:
            - `str`: The name of the customer on the credit card.
        """
        return self._customer

    def get_bank(self) -> str:
        """Return the name of the bank on the credit card.

        Args:
            - `None`

        Returns:
            - `str`: The name of the bank on the credit card.
        """
        return self._bank

    def get_account(self) -> str:
        """Return the account identifier of the card as a string.

        Args:
            - `None`

        Returns:
            - `str`: The account identifier on the card.
        """
        return self._account

    def get_limit(self) -> Decimal:
        """Return the current limit of the credit card.

        Args:
            - `None`

        Returns:
            - `float`: The current limit of the credit card.
        """
        return self._limit

    def get_balance(self) -> Decimal:
        """Return the current balance of the credit card.

        Args:
            - `None`

        Returns:
            - `float`: The current balance of the credit card.
        """
        return self._balance

    def charge(self, price: Decimal) -> bool:
        """Charge given price to the card if there is sufficient credit limit.

        Args:
            - `price` (`Decimal`): The price of the item being charged to the credit card.

        Returns:
            - `bool`: `True` if charge was processed. `False` if charge was denied.
        """
        # If charge would exceed limit, cannot accept charge
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount: Decimal) -> None:
        """Process customer payment that reduces balance.

        Args:
            - `amount` (`float`): The amount that the customer is paying.

        Returns:
            - `None`
        """
        self._balance -= amount


from decimal import Decimal

# Calling the class constructor to create a new instance of CreditCard
# --------------------------------------------------------------------
cc1: CreditCard = CreditCard(
    "John Doe", "First Bank", "5432.1098.7654.3210", Decimal(1000)
)
cc2: CreditCard = CreditCard(
    customer="Mary Bell",
    bank="Chase",
    account="0987.6543.2109.8765",
    limit=Decimal(500),
    starting_balance=Decimal("100.1455"),
)

print(f"CC1 Customer: {cc1.get_customer()}. Balance: ${cc1.get_balance():.2f}")
print(f"CC2 Customer: {cc2.get_customer()}. Balance: ${cc2.get_balance():.2f}")


if __name__ == "__main__":
    # Variables
    wallet: list[CreditCard] = []

    # Append credit cards to the wallet
    wallet.append(
        CreditCard(
            "John Bowman", "California Savings", "5391 0375 9387 5309", Decimal(2500)
        )
    )
    wallet.append(
        CreditCard(
            "John Bowman", "California Federal", "3485 0399 3395 1954", Decimal(3500)
        )
    )
    wallet.append(
        CreditCard(
            "John Bowman", "California Finance", "5391 0375 9387 5309", Decimal(5000)
        )
    )

    # Test charge
    for val in range(1, 17):
        wallet[0].charge(Decimal(val))
        wallet[1].charge(2 * Decimal(val))
        wallet[2].charge(3 * Decimal(val))

    # Test methods on all credit cards
    for c in range(3):
        print(f"Customer = {wallet[c].get_customer()}")
        print(f"Bank = {wallet[c].get_bank()}")
        print(f"Account = {wallet[c].get_account()}")
        print(f"Limit = {wallet[c].get_limit()}")
        print(f"Balance = {wallet[c].get_balance()}")

        while wallet[c].get_balance() > Decimal(100):
            wallet[c].make_payment(Decimal(100))
            print(f"New balance = {wallet[c].get_balance()}")

        print()


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


# Testing a vector

# Construct five-dimensional <0, 0, 0, 0, 0>
vec: Vector = Vector(5)

# <0, 23, 0, 0, 0> (based on use of __setitem__)
vec[1] = 23

# <0, 23, 0, 0, 45> (also via __setitem__)
vec[-1] = 45

print(f"{vec = }")
print(f"{vec[4] = }")  # (via __getitem__)


# <0, 46, 0, 0, 90> (via __add__)
u: Vector = vec + vec
print(f"{u = }")


total: int = 0

# implicit iteration via len and getitem
# However, this is currently not compatible with mypy
# It is better to implement `__iter__` directly
# for entry in vec:
#     total += entry
# print(f"{total = }"")


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


from decimal import Decimal


class PredatoryCreditCard(CreditCard):
    """An extension to `CreditCard` that compounds interest and fees."""

    def __init__(
        self, customer: str, bank: str, accnt: str, limit: Decimal, apr: Decimal
    ) -> None:
        """Create a new `PredatoryCreditCard` instance.

        Args:
            - `customer` (`str`): The name of the customer (e.g., John Bowman).
            - `bank` (`str`): The name of the bank (e.g., California Savings).
            - `acnt` (`str`): The acount identifier (e.g., 5391 0375 9387 5309).
            - `limit` (`float`): Credit limit (measured in dollars).
            - `apr` (`float`): Annual percentage rate (e.g., 0.0825 for 8.25% APR).

        The initial balance is zero.
        """
        # Call super constructor
        super().__init__(customer=customer, bank=bank, account=accnt, limit=limit)
        self._apr: Decimal = apr

    def charge(self, price: Decimal) -> bool:
        """Charge a given price to the card, assuming sufficient credit limit.

        Args:
            - `price` (`Decimal`): The price that is charged to the credit card.

        Returns:
            - `bool`: `True` if charge was processed, `False` and assess 5 fee if charge is denied.
        """
        # Call inherited method
        _success: bool = super().charge(price)

        if not _success:
            # Assess penalty
            self._balance += 5

        # Caller expects return value
        return _success

    def process_month(self) -> None:
        """Assess monthly interest on outstanding balance."""
        if self._balance > 0:
            # If positive balance, convert APR to monthly multiplicative factor
            monthly_factor: Decimal = Decimal(
                f"{pow(1 + self._apr, Decimal(1) / Decimal(12))}"
            )
            self._balance *= monthly_factor


# UNIT TESTS
# ----------
if __name__ == "__main__":
    # Variables
    wallet2: list[PredatoryCreditCard] = []

    # Append credit cards to the wallet
    wallet2.append(
        PredatoryCreditCard(
            "John Bowman",
            "California Savings",
            "5391 0375 9387 5309",
            Decimal(2500),
            Decimal("0.0825"),
        )
    )
    wallet2.append(
        PredatoryCreditCard(
            "John Bowman",
            "California Federal",
            "3485 0399 3395 1954",
            Decimal(3500),
            Decimal("0.0525"),
        )
    )
    wallet2.append(
        PredatoryCreditCard(
            "John Bowman",
            "California Finance",
            "5391 0375 9387 5309",
            Decimal(5000),
            Decimal("0.0225"),
        )
    )

    # Test charge
    for val in range(1, 17):
        wallet2[0].charge(Decimal(val))
        wallet2[1].charge(2 * Decimal(val))
        wallet2[2].charge(3 * Decimal(val))

    # Test methods on all credit cards
    for c in range(3):
        print(f"Customer = {wallet2[c].get_customer()}")
        print(f"Bank = {wallet2[c].get_bank()}")
        print(f"Account = {wallet2[c].get_account()}")
        print(f"Limit = {wallet2[c].get_limit()}")
        print(f"Balance (Before Month Processing) = {wallet2[c].get_balance()}")
        wallet2[c].process_month()
        print(f"Balance (After Month Processing) = {wallet2[c].get_balance()}")

        while wallet2[c].get_balance() > Decimal(100):
            wallet2[c].make_payment(Decimal(100))
            print(f"New balance = {wallet2[c].get_balance()}")

        print()


"""
Module: progression.py
This is a simple implementation of Progression classes.
"""


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


# IMPORT MODULES
# --------------
from abc import ABCMeta, abstractmethod  # Need these definitions
from typing import Any


# DEFINE CLASS
# ------------
class AbSequence(metaclass=ABCMeta):
    """Our own version of collections.Sequence abstract base class."""

    @abstractmethod
    def __len__(self) -> int:
        """Return the length of the sequence."""

    @abstractmethod
    def __getitem__(self, j: int) -> Any:
        """Return the element at index `j` of the sequence."""

    # Concrete Method: Template Method
    def __contains__(self, val: Any) -> bool:
        """Return `True` if `val` found in the sequence. `False` otherwise."""
        for j in range(len(self)):
            if self[j] == val:
                # Found match
                return True
        return False

    # Concrete Method: Template Method
    def index(self, val: Any) -> int:
        """Return leftmost index at which `val` is found (or raise `ValueError`)."""
        for j in range(len(self)):
            if self[j] == val:
                # Leftmost match
                return j
        # Never found a match
        raise ValueError("value not in sequence.")

    # Concrete Method: Template Method
    def count(self, val: Any) -> int:
        """Return the number of elements equal to given value."""
        k: int = 0
        for j in range(len(self)):
            if self[j] == val:
                # Found a match
                k += 1
        return k


# IMPORT MODULES
# --------------
from decimal import Decimal
from typing import Final


# DEFINE CLASS
# ------------
class PredatoryCreditCardV2(CreditCard):
    """An extension to `CreditCard` that compounds interest and fees."""

    # Class Data Members
    # ------------------
    _OVERLIMIT_FEE: Final[Decimal] = Decimal(5)

    # Class Methods
    # -------------
    def __init__(
        self, customer: str, bank: str, accnt: str, limit: Decimal, apr: Decimal
    ) -> None:
        """Create a new predatory credit card instance.

        Args:
            - `customer` (`str`): The name of the customer (e.g., John Bowman).
            - `bank` (`str`): The name of the bank (e.g., California Savings).
            - `accnt` (`str`): The acount identifier (e.g., 5391 0375 9387 5309).
            - `limit` (`float`): Credit limit (measured in dollars).
            - `apr` (`float`): Annual percentage rate (e.g., 0.0825 for 8.25% APR).

        The initial balance is zero.
        """
        super().__init__(customer, bank, accnt, limit)  # call super constructor
        self._apr: Decimal = apr

    def charge(self, price: Decimal) -> bool:
        """Charge given price to the card, assuming sufficient credit limit.

        Args:
            - `price` (`float`): The price that is charged to the credit card.

        Returns:
            - `bool`: `True` if charge was processed, `False` and assess 5 fee if charge is denied.
        """
        # Call inherited method
        _success: bool = super().charge(price)

        if not _success:
            # Assess penalty
            self._balance += PredatoryCreditCardV2._OVERLIMIT_FEE

        # Caller expects return value
        return _success

    def process_month(self) -> None:
        """Assess monthly interest on outstanding balance."""
        if self._balance > 0:
            # If positive balance, convert APR to monthly multiplicative factor
            monthly_factor: Decimal = Decimal(
                f"{pow(1 + self._apr, Decimal(1) / Decimal(12))}"
            )
            self._balance *= monthly_factor


class Color:
    """A class representing a color using RGB."""

    def __init__(self, r: int, g: int, b: int) -> None:
        """Create a new instance of Color.

        Args:
            - `r (`int`): The value for Red.
            - `g` (`int`): The value for Green.
            - `b` (`int`): The value for Blue.
        """
        self._r: int = r
        self._g: int = g
        self._b: int = b

    def __str__(self) -> str:
        """Returns a string representing the color.

        Returns:
            - `str`: A string representing the color.
        """
        return f"Color({self._r}, {self._g}, {self._b})"

    def __repr__(self) -> str:
        """Returns a string representing the color.

        Returns:
            - `str`: A string representing the color.
        """
        return f"Color({self._r}, {self._g}, {self._b})"


# A list of warmtone colors: Orange, Brown
warmtones: list[Color] = [Color(249, 124, 43), Color(169, 163, 52)]
print(f"{warmtones = }")


# Make palette a SHALLOW COPY of warmtone colors
#   We want to subsequently be able to add additional colors to palette, or
#   to modify or remove some of the existing colors, without affecting the contents of
#   warmtones (Not an alias)
warm_palette: list[Color] = list(warmtones)
print(f"{warm_palette = }")


# IMPORT MODULES
# --------------
from copy import copy, deepcopy

# Make palette a SHALLOW COPY of warmtone colors
#   We want to subsequently be able to add additional colors to palette, or
#   to modify or remove some of the existing colors, without affecting the contents of
#   warmtones (Not an alias)
warm_palette_shallow_copy: list[Color] = copy(warmtones)
print("Shallow Copy:", warm_palette_shallow_copy)


# Make palette a DEEP COPY of warmtone colors
#   We want to subsequently be able to add additional colors to palette, or
#   to modify or remove some of the existing colors, without affecting the contents of
#   warmtones (Not an alias)
warm_palette_deep_copy: list[Color] = deepcopy(warmtones)
print("Deep Copy:", warm_palette_deep_copy)
