#!/usr/bin/env python
# coding: utf-8

"""
Module: gpa.py
This program computes a student's GPA based on letter grades entered by a user.
"""

# IMPORT MODULES
# --------------
from typing import Final, TypeAlias

# TYPE ALIASES
# ------------
GradeMap: TypeAlias = dict[str, float]

# CONSTANTS
# ---------
# Map of letter grades to point values
POINTS: Final[GradeMap] = {
    "A+": 4.0,
    "A": 4.0,
    "A-": 3.67,
    "B+": 3.33,
    "B": 3.0,
    "B-": 2.67,
    "C+": 2.33,
    "C": 2.0,
    "C-": 1.67,
    "D+": 1.33,
    "D": 1.0,
    "F": 0.0,
}

# VARIABLES
# ---------
num_courses: int = 0
total_points: float = 0
grade: str = ""

# Print welcome and instructions
print("--- Welcome to the GPA Calculator ---")
print("-------------------------------------")
print("Please enter all your letter grades, one per line.")
print("Enter a blank line to designate the end.")

# Loop to get user inputs
while True:
    # Read line from user
    grade = input("Enter the next grade or leave empty if done:").strip()

    # Handle when empty line is entered
    if grade == "":
        break

    # Handle when unrecognized grade is entered
    elif grade not in POINTS:
        print(f"Unknown grade '{grade}': It will be skipped and ignored.")

    # For all other cases
    else:
        num_courses += 1
        total_points += POINTS[grade]

# Calculate GPA: Avoid division by zero
if num_courses > 0:
    print(f"- Total count of courses: {num_courses}")
    print(f"- Final GPA: {total_points / num_courses:.3}")


# Declaring
# ---------
# Possible when using Type-Hints
# But using these without assigning first results in `NameError`
age: int
name: str

# Assigning
# ---------
# Without Type-Hints, this would be the same as Declaring and Assigning
age = 38
# age points to --> In Memory Value: {type: int, value: 38}
name = "John"
# name points to --> In Memory Value: {type: str, value: John}

# Declaring and Assigning
# -----------------------
is_alive: bool = True
# is_alive points to --> In Memory Value: {type: bool, value: True}

print(f"{age = }")
print(f"{name = }")
print(f"{is_alive = }")


"""
Module: py_keywords.py
This program lists all the keywords in a Python version.
"""

# IMPORT MODULES
# --------------
from keyword import kwlist
from platform import python_version
from typing import Final, List, Tuple, TypeAlias

# TYPE ALIASES
# ------------
LowerCaseKwd: TypeAlias = Tuple[str, str]
Kwd: TypeAlias = str

# CONSTANTS
# ---------
LOWERED_KWS: Final[List[LowerCaseKwd]] = list(map(lambda kw: (kw, kw.lower()), kwlist))
SORTED_LOWERED_KWS: Final[List[LowerCaseKwd]] = sorted(
    LOWERED_KWS, key=lambda tup: tup[1]
)
SORTED_KWS: Final[List[Kwd]] = [kw for (kw, _) in SORTED_LOWERED_KWS]

# Print the summary
print(f"There are {len(SORTED_KWS)} Keywords in Python {python_version()}:")

# Print the list of keywords
print(" | ".join(SORTED_KWS))


# IMPORT MODULES
# --------------
from typing import Final

# This is an identifier that points to the value 98.5 in memory
ACTUAL_TEMP: Final[float] = 98.5
print(f"{ACTUAL_TEMP = }")
# In_Memory: ACTUAL_TEMP = 0xe2d4a1 --> { type: float, value: 98.5 }

# This is an alias that points to the same value 98.5 in memory
today_temp: float = ACTUAL_TEMP
print(f"{today_temp = }")
# In_Memory: today_temp = 0xe2d4a1 --> { type: float, value: 98.5 }

# Reassigning a new value to an alias breaks the alias
# because it would then point to a different value in memory
today_temp = today_temp + 5
print("Changing today_temp:", today_temp)
print(f"{ACTUAL_TEMP = }")
# In_Memory: today_temp = 0xffe321 --> { type: float, value: 103.5 }
# In_Memory: ACTUAL_TEMP = 0xe2d4a1 --> { type: float, value: 98.5 }


# IMPORT MODULES
# --------------
from typing import Final, TypeAlias

# TYPE ALIASES
# ------------
Employee: TypeAlias = dict[str, str | int | bool]

# CONSTANTS
# ---------
# Literal form of instantiating an integer
AGE: Final[int] = 36

# Literal form of instantiating a string
GREETINGS: Final[str] = "Greetings, Peasants!"

# Literal form of instantiating a dictionary
EMPLOYEE: Final[Employee] = {
    "first_name": "John",
    "last_name": "Smith",
    "dob": "1970-01-01",
    "is_active": True,
    "lucky_number": 11,
}

# Showing result
print(f"{AGE = }")
print(f"{GREETINGS = }")
print(f"{EMPLOYEE = }")


# IMPORT MODULES
# --------------
from typing import List

# Example of a string
some_str: str = "Hello my friend!"

# We can sort the letters in the string using sorted()
# By doing so, we get back a new list instead
list_str: List[str] = sorted(some_str)

# The original argument (some_str) is left untouched
print(f"{some_str = }")

# sorted() creates and return a new list
print(f"{list_str = }")


# IMPORT MODULES
# --------------
from typing import List

# Example of a list
list_int: List[int] = [34, 67, 4, -1, 30, 255, -300]

# Calling a list method
# Unlike sorted(), this does not return a new list but transforms the list itself
list_int.sort()

# Showing the list after being sorted
print(f"{list_int = }")


# IMPORT MODULES
# --------------
from typing import Final

# CONSTANTS
# ---------
# Exampe of a string
HELLO: Final[str] = "hello world!"

# Chaining methods
# A string is immutable: Each method call returns a new string
print(f"{HELLO.capitalize().startswith('h') = }")


# IMPORT MODULES
# --------------
from typing import Final, Set

# CONSTANTS
# ---------
# Define a set of characters from a string
DISTINCT_CHARS: Final[Set[str]] = set(
    "Hello World! This is an example of a string".lower()
)

# Print the value of the set
print(f"{DISTINCT_CHARS = }")


# IMPORT MODULES
# --------------
from typing import List

# VARIABLES
# ---------
alpha: List[int] = [1, 2, 3]
beta: List[int] = alpha  # An alias of alpha
gamma: List[int] = alpha  # Another alias of alpha

beta += [4, 5]  # Extends the original list with two more elements
gamma = gamma + [6, 7]  # Breaks alias: Reassigns to a NEW list [1, 2, 3, 4, 5, 6, 7]

print(f"{alpha = }")  # Will be [1, 2, 3, 4, 5]
print(f"{beta = }")  # Will be [1, 2, 3, 4, 5]
print(f"{gamma = }")  # Will be [1, 2, 3, 4, 5, 6, 7]


# IMPORT MODULES
# --------------
from typing import Final

# CONSTANTS
# ---------
YOUR_AGE: Final[int] = 17

# Conditional
if YOUR_AGE >= 18:
    print("You are an adult")
elif 0 < YOUR_AGE < 18:
    print("You are not old enough")
else:
    print("Are you even born yet?")


# IMPORT MODULES
# --------------
from typing import Final

# CONSTANTS
# ---------
USER_CHOICE: Final[str] = "Pineapple"

# Conditional using match
match USER_CHOICE:
    case "Apple":
        print("An apple a day keeps the doctor away.")
    case "Banana" | "Papaya" | "Orange":
        print("Yellow fruits are also good for your health!")
    case "Pineapple":
        print("Pineapple is not technically a fruit but a berry")
    case _:  # Optional default if no match found. If skipped, then None
        print("What is your favorite fruit?")


# Example of `while` Loop
# -----------------------
digit_data: str = "9876543210"
digit: int = 9

while str(digit) in digit_data:
    print(digit, end=" ")
    digit -= 1


# Example of `for` Loop
# ---------------------
digit_data = "9876543210"

for dgt in digit_data:
    print(dgt, end=" ")
    dgt = "1"  # This reassignment has no effect on original data or next value


# Finding the Biggest Digit in a String
# -------------------------------------
digit_data = "1234567890"
biggest: int = 0

for el in digit_data:
    dt: int = int(el)
    if dt > biggest:
        biggest = dt

print(f"{biggest} is the biggest digit in {digit_data}")


# Using for index in range()
# --------------------------
digit_data = "9876543210"

for index in range(len(digit_data)):
    print(index, end=" ")


# Using for idx, val in enumerate()
# ---------------------------------
digit_data = "9876543210"

print("idx   val")
print("---   ---")
for idx, val in enumerate(digit_data):
    print(f" {idx} --> {val}")


# Example of using `break`
# ------------------------
digit_data = "9876543210"

for dgt in digit_data:
    # Immediately terminate when reaching 4
    if dgt == "4":
        break
    print(dgt, end=" ")


# Example of using `continue`
# ---------------------------
digit_data = "9876543210"

for dgt in digit_data:
    # Skip all even numbers
    if int(dgt) % 2 == 0:
        continue
    print(dgt, end=" ")


# IMPORT MODULES
# --------------
from typing import Iterable, TypeVar

# CUSTOM TYPES
# ------------
TCount = TypeVar("TCount", str, int, float, bool)


# Example of a function
# ---------------------
def count(target: TCount, data: Iterable[TCount]) -> int:
    """Counts the number of occurrences of a given `target` value within any form of iterable `data` set.

    Args:
        `target` (`TypeVar("TCount", str, int, float, bool)`): The target value
        `data` (`Iterable[TCount]`): The iterable set

    Returns:
        `int`: The number of occurences of `target` within `data`

    The `target` can be any value of type `str`, `int`, `float`, or `bool`.
    """

    # The count of occurences
    count: int = 0

    # Loop through the items in the data
    for item in data:
        if item == target:
            count += 1

    # Return count of occurences
    return count


# Example of Function Runtime
# ---------------------------
print(f'{count("a", "abracadabra") = }')


def contains(target: str, data: str) -> bool:
    """Checks whether a `target` string is contained in another `data` string or not.

    Args:
        `target` (`str`): The string to check if being contained
        `data` (`str`): The string to check into if it contains the `target` string

    Returns:
        `bool`: Whether the `target` string is contained in `data` or not
    """

    for item in data:
        if item == target:
            # If here, the item was found
            return True

    # If here, then not found
    return False


print(f'{contains(target="zzz", data="Hello World") = }')


# IMPORT MODULES
# --------------
from typing import List, TypeVar

# CUSTOM TYPES
# ------------
TNumeric = TypeVar("TNumeric", int, float)


def scale(data: List[TNumeric], factor: TNumeric) -> None:
    """Multiply all entries of a numeric `data` set by a given `factor`.

    Args:
        `data` (`List[TNumeric]`): A list of numeric data to multiply
        `factor` (`TNumeric`): The factor to multiply by
    """

    for j in range(len(data)):
        data[j] *= factor


primes_4: List[int] = [2, 3, 5, 7]
print(f"Before scale(primes_4, 50): {primes_4 = }")
# List is a mutable object
scale(primes_4, 50)
# The state of the actual parameter have been affected
print(f"After scale(primes_4, 50): {primes_4 = }")


# IMPORT MODULES
# --------------
from typing import Final, List, TypeAlias

# CUSTOM TYPES
# ------------
GradeMap2: TypeAlias = dict[str, float]


def compute_gpa(
    grades: List[str],
    points: GradeMap2 = {
        "A+": 4.0,
        "A": 4.0,
        "A-": 3.67,
        "B+": 3.33,
        "B": 3.0,
        "B-": 2.67,
        "C+": 2.33,
        "C": 2.0,
        "C-": 1.67,
        "D+": 1.33,
        "D": 1.0,
        "F": 0.0,
    },
) -> float:
    """Computes a student's GPA based on letter grades entered by a user.

    Args:
        `grades` (`List[str]`): A list of letter grades
        `points` (`GradeMap`, optional): A mapping of letter grades to equivalent GPA point. Defaults to a given GradeMap.

    Returns:
        `float`: The final GPA

    While the point system is somewhat common, it may not agree with the system used by all schools.
    Allowing `points` to be optional allows flexibility to either use the default point system or pass a custom mapping.
    """

    # Declare and initialize variables
    num_courses: int = 0
    total_points: float = 0

    for g in grades:
        if g in points:
            # It is a recognizable grade
            num_courses += 1
            total_points += points[g]

    return total_points / num_courses


print(f'{compute_gpa(["A", "A+", "B+", "B"]) = }')


# Example of Asking User Input
# ----------------------------
user_age: int

try:
    user_age = int(input("Enter your age in years: "))
except ValueError:
    print("That was not a valid age. Defaulting age to average: 25.")
    user_age = 25

# Heart Rates formula as per Med Sci Sports Exerc
max_heart_rate: float = 206.9 - (0.67 * user_age)
target_heart_rate: float = 0.65 * max_heart_rate
print(f"If your age is {user_age}, ", end="")
print(f"then your target fat-burning heart rate is {target_heart_rate:.2f}.")


# IMPORT MODULES
# --------------
# from typing import TypeVar

# CUSTOM TYPES
# ------------
# TNumeric = TypeVar("TNumeric", int, float)


def sqrt_func(x: TNumeric) -> None:
    # x must be a number
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric")

    # x must be non-negative
    if x < 0:
        raise ValueError("x cannot be negative")

    # do the real work here...


# IMPORT MODULES
# --------------
from collections.abc import Iterable

# from typing import TypeVar

# TYPE VARS
# ---------
# TNumeric = TypeVar("TNumeric", int, float)


def sum(values: Iterable[TNumeric]) -> TNumeric:
    """Example of the sum function with extreme checks"""

    if not isinstance(values, Iterable):
        raise TypeError("Parameter must be an iterable type")

    total: TNumeric = 0
    for v in values:
        if not isinstance(v, (int, float)):
            raise TypeError("Elements must be numeric")
        total += v
    return total


# IMPORT MODULES
# --------------
from typing import Any


def sum2(values: Any) -> Any:
    """Example of the sum function without checks"""
    total: Any = 0
    for v in values:
        total += v
    return total


# IMPORT MODULES
# --------------
from io import TextIOWrapper

try:
    fp: TextIOWrapper = open("bad_file_example.txt")
except IOError as e:
    print(f"Unable to open the file:\n{e}")


some_age: int = -1  # an initially invalid choice

while some_age <= 0:
    try:
        some_age = int(input("Enter your age in years:"))
        if some_age <= 0:
            print("Your age must be positive")
    # Handle multiple exceptions at once
    except (ValueError, EOFError):
        print("Invalid response")


some_age = -1  # an initially invalid choice

while some_age <= 0:
    try:
        some_age = int(input("Enter your age in years:"))
        if some_age <= 0:
            print("Your age must be positive")
    except ValueError:
        print("That is an invalid age specification")
    except EOFError:
        print("There was an unexpected error reading input.")
        raise  # let's re-raise this exception


# IMPORT MODULES
# --------------
from typing import Iterator

nums_ints: List[int] = [1, 2, 3, 4, 5]  # Iterable
iter_nums: Iterator[int] = iter(nums_ints)  # Iterator

print(next(iter_nums), end=" ")  # => 1
print(next(iter_nums), end=" ")  # => 2
print(next(iter_nums), end=" ")  # => 3
print(next(iter_nums), end=" ")  # => 4
print(next(iter_nums), end=" ")  # => 5


# IMPORT MODULES
# --------------
from typing import List


def factors_func(n: int) -> List[int]:
    """A traditional function that computes factors.

    Args:
        - `n` (`int`): The integer that we want to compute the factors of.

    Returns:
        `List[int]`: The factors of the given number.
    """

    # Store factors in a new list
    factors: List[int] = []

    for k in range(1, n + 1):
        if n % k == 0:  # Divides evenly, thus k is a factor
            # Add k to the list of factors
            factors.append(k)

    # Return the entire list
    return factors


print(factors_func(100))


# IMPORT MODULES
# --------------
from typing import Generator


def factors_gen(n: int) -> Generator[int, None, None]:
    """A generator that computes factors

    Args:
        - `n` (`int`): The integer that we want to compute the factors of.

    Yields:
        `Generator[int, None, None]`: Generator of the factors of `n`
    """

    for k in range(1, n + 1):
        if n % k == 0:  # Divides evenly, thus k is a factor
            # Yield this factor as next result
            yield k


for x in factors_gen(100):  # Creates an instance of the generator, which is an iterator
    print(x, end=" ")


def factors_gen_2(n: int) -> Generator[int, None, None]:
    """A generator that computes factors

    Args:
        - `n` (`int`): The integer that we want to compute the factors of.

    Yields:
        `Generator[int, None, None]`: Generator of the factors of `n`
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


for x in factors_gen_2(100):
    print(x, end=" ")


def fibonacci_gen() -> Generator[int, None, None]:
    """A generator of fibonaci sequence

    Yields:
        `Generator[int, None, None]`: The sequence of Fibonacci numbers
    """

    # Declare and initialize variables
    a: int = 0
    b: int = 1

    while True:  # keep going...
        yield a  # report value, a, during this pass
        future = a + b
        a = b  # this will be next value reported
        b = future  # and subsequently this


# This would be an infinite loop without an if condition
for x in fibonacci_gen():
    print(x, end=" ")
    # Use a condition to eventually break
    if x > 1000:
        break


# Absolute Value Using If-Else
def abs(n: TNumeric) -> TNumeric:
    """Return the absolute value of a given number

    Args:
        - `n` (`TNumeric`): The number that we want the absolute value of

    Returns:
        `TNumeric`: The value of the absolute value
    """

    if n >= 0:
        return n
    else:
        return -n


print(abs(-67))


# Absolute Value Using Conditional Expression
def abs_val(n: TNumeric) -> TNumeric:
    """Return the absolute value of a given number

    Args:
        - `n` (`TNumeric`): The number that we want the absolute value of

    Returns:
        `TNumeric`: The value of the absolute value
    """

    return n if n >= 0 else -n


print(abs_val(-100))


# IMPORT MODULES
# --------------
from typing import List


# Squares using for-loop
def squares(n: int) -> List[int]:
    """Return a list of `n` squared numbers starting from 1.

    Args:
        - `n` (`int`): The count of squares to return in the list

    Returns:
        `List[int]`: List containing the squares
    """

    # Declare and initialize variables
    squares: List[int] = []

    for k in range(1, n + 1):
        squares.append(k * k)

    return squares


print(squares(10))


# IMPORT MODULES
# --------------
from typing import List


# Squares using List Comprehension
def squares_comp(n: int) -> List[int]:
    """Return a list of `n` squared numbers starting from 1.

    Args:
        - `n` (`int`): The count of squares to return in the list

    Returns:
        `List[int]`: List containing the squares
    """
    return [k * k for k in range(1, n + 1)]


print(squares_comp(10))


# IMPORT MODULES
# --------------
from typing import List


# List of factors for a given integer
def factors_func_2(n: int) -> List[int]:
    """A traditional function that computes factors.

    Args:
        - `n` (`int`): The integer that we want to compute the factors of.

    Returns:
        `List[int]`: The factors of the given number.
    """

    return [k for k in range(1, n + 1) if n % k == 0]


print(factors_func_2(100))


# List Comprehension using []
print([k * k for k in range(10)])


# Set comprehension using {}: There is no order expected
print({k * k for k in range(10)})


# Generator comprehension using ()
gen_int: Generator[int, None, None] = (k * k for k in range(10))

for x in gen_int:
    print(x, end=" ")


# Dictionary comprehension
print({k: k * k for k in range(10)})


# IMPORT MODULES
# --------------
from typing import Tuple


def simple_return() -> Tuple[int, ...]:
    """Return a demo packed tuple.

    Returns:
        `Tuple[int]`: A tuple of integers
    """
    return 1, 2, 3, 4


# Declaring the variables types in advance
a: int
b: int
c: int
d: int

# Tuple-unpacking values from a function
a, b, c, d = simple_return()
# a = 1; b = 2; c = 3; d = 4

print(a, b, c, d)


a, b = divmod(94, 5)
print(a, b)


from typing import Any

person: dict[str, Any] = {"fname": "John", "lname": "Appleseed", "age": 30}

# Tuple-unpacking values from a dictionary
for k, v in person.items():
    print(k, v)


# Declaring the variables types in advance
x0: int
y0: int
z0: int

# Simulataneous assignment
x0, y0, z0 = 6, 2, 5

print(x0, y0, z0)


x0, y0 = y0, x0
print(x0, y0)


# Declare variable
temp: int

# Value swapping is equivalent to the following snippet
temp = y0
y0 = x0
x0 = temp
print(x0, y0)


def fibonacci_gen_2() -> Generator[int, None, None]:
    """A generator of fibonaci sequence

    Yields:
        `Generator[int, None, None]`: The sequence of Fibonacci numbers
    """
    # Declare variables
    a: int
    b: int

    # Initialize variable
    a, b = 0, 1

    while True:  # keep going...
        yield a  # report value, a, during this pass
        a, b = b, a + b


# This would be an infinite loop without an if condition
for x in fibonacci_gen_2():
    # Use a condition to eventually break
    if x > 1000:
        break
    print(x, end=" ")


def simple_test_func() -> None:
    x: int = 3
    y: int = 4

    # Print a list of all local variables
    print(f"dir(): {dir()}")

    # Print a key:value mapping of all local variables
    print(f"vars(): {vars()}")


simple_test_func()


# IMPORT MODULES
# --------------
import math

print(f"PI = {math.pi}")
print(f"E = {math.e}")
print(f"sqrt(8) = {math.sqrt(8)}")
