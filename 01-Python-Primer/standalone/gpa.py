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
done: bool = False
grade: str = ""

# Print welcome and instructions
print("--- Welcome to the GPA Calculator ---")
print("-------------------------------------")
print("Please enter all your letter grades, one per line.")
print("Enter a blank line to designate the end.")

# Loop to get user inputs
while not done:
    # Read line from user
    grade = input("Enter the next grade or leave empty if done:").strip()

    # Handle when empty line is entered
    if grade == "":
        done = True

    # Handle when unrecognized grade is entered
    elif grade not in POINTS:
        print(f'Unknown grade "{grade}": It will be skipped and ignored.')

    # For all other cases
    else:
        num_courses += 1
        total_points += POINTS[grade]

# Calculate GPA: Avoid division by zero
if num_courses > 0:
    print(f"- Total count of courses: {num_courses}")
    print(f"- Final GPA: {total_points / num_courses:.3}")
