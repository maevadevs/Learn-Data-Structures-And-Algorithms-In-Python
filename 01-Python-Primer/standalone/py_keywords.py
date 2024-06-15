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
