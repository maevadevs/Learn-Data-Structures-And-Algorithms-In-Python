import os
import shutil
from typing import Final

############################################################################################################
# FILE: clean.py
# PROJECT: Standalone Script
# PURPOSE: Automates the following for a directory from which it is run:
#   1. Check the directory and all subdirectories for the listed objects to delete
#   2. After user confirmation, recursively delete all listed paths
# BEFORE RUNNING: Make sure to define the following variables below:
#   1. $ITEMS_TO_DELETE: The objects to delete throughout the directory and subdirectories
# PARAMETERS: NONE
# EXAMPLE CALL: Make sure to call this script from the project root directory from Powershell:
#   > python clean.py
############################################################################################################
#   1.0.0   2023-03-22      Maeva Ralafiarindaza    :   INITIAL RELEASE
#   2.0.0   2024-05-11      Maeva Ralafiarindaza    :   Converted from .ps1 to .py
############################################################################################################
# ACTION ITEMS: List all objects to delete throughout the directory and subdirectories
ITEMS_TO_DELETE: Final[list[str]] = [
    "__pycache__",
    ".mypy_cache",
    ".pyc",
    ".ipynb_checkpoints",
    ".ruff_cache",
]
############################################################################################################

# Check for all the elements-to-delete through the entire directory and subdirectories
# Get their full-paths
# for item in ITEMS_TO_DELETE:
# Get all the objects that match the name of the item
objs: list[tuple[str, str]] = []
root: str = os.getcwd()
to_del: str
confirmed: str

# List of subdirectories
for path, subdirs, _ in os.walk(root):
    for subdir in subdirs:
        if subdir in ITEMS_TO_DELETE:
            to_del = os.path.join(path, subdir)
            objs.append(("DIR", to_del))

# List of files
for path, _, files in os.walk(root):
    for file in files:
        if file in ITEMS_TO_DELETE:
            to_del = os.path.join(path, file)
            objs.append(("FILE", to_del))

if len(objs) > 0:
    # Show the list of directories to delete if any
    print("DIRS TO DELETE")
    for typ, path in objs:
        if typ == "DIR":
            print(path)
    print()

    # Show the list of files to delete if any
    print("FILES TO DELETE")
    for typ, path in objs:
        if typ == "FILE":
            print(path)
    print()

    # Ask usr confirmation to preoceed with deletion
    confirmed = input("Proceed? (Enter 'y' to confirm, else aborting): ")

    if confirmed.lower() == "y":
        print("Deleting...")
        for typ, path in objs:
            if typ == "DIR":
                shutil.rmtree(path)
            if typ == "FILE":
                os.remove(path)
        print("Objects have been deleted.")
        print()
    else:
        print("Aborting deletion... No object deleted.")
        print()
else:
    print("No objects to delete found.")
    print()
