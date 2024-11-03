# IMPORT MODULES
# --------------
from typing import TypeAlias

# CUSTOM TYPES
# ------------
GradeMap2: TypeAlias = dict[str, float]


def compute_gpa(
    grades: list[str],
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
        - `grades` (`List[str]`): A list of letter grades.
        - `points` (`GradeMap`, optional): A mapping of letter grades to equivalent GPA point. Defaults to a given GradeMap.

    Returns:
        - `float`: The final GPA.

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
