##################################################################################################
# FILE: nb2py.py
# PROJECT: Standalone Script
# PURPOSE: This script automates the following for a Python project:
#   1. Convert a .ipynb file into .py
#   2. Optional: Ensure that .py files are using static types correctly using mypy
#   3. Optional: Keep or remove the jupyter notebook cells in the .py file
#   4. Optional: Keep or remove the jupyter notebook markdown (comments) in the .py file
# PARAMETERS:
#   1. Subfolder that contains the .ipynb file to convert (required)
#   2. Filename of the .ipynb file without the extension (required)
#   3. The script is applying mypy checks by default. To skip mypy checks, set -nomypy flag
#   4. Jupyter notebook cells are removed by default. To keep the cells, set -keepcells flag
#   5. Formatting using Black is applied by default. To skip formatting, set -noformat flag
# EXAMPLE CALLS:
#   - Make sure to call this script from the project root directory from the shell:
#       > python nb2py.py notes notebook *> log.txt
#       > python nb2py.py not* notebook --nomypy
#       > python nb2py.py not* notebook --nomypy --keepcells --keepmd --noformat
##################################################################################################
#   1.0.0  2023-03-15  Maeva Ralafiarindaza : INITIAL RELEASE
#   1.1.0  2023-03-25  Maeva Ralafiarindaza : Allow wildcard * in args and resolve
#                                             Add -nomypy, -keepcells, and -keepmd optional params
#   1.2.0  2023-04-21  Maeva Ralafiarindaza : Add -noformat optional params
#   2.0.0  2023-05-29  Maeva Ralafiarindaza : Convert to setup for Anaconda
#   3.0.0  2024-05-06  Maeva Ralafiarindaza : Convert into Python script
##################################################################################################
# Imports
import re
import black
import mypy
import mypy.api
import nbformat

# import subprocess
from os import path
from pathlib import Path
from sys import argv, exit as sysexit
from typing import Any, Final
from nbconvert import PythonExporter

##################################################################################################
# ACTION ITEM: Input the name of the project folder
PROJ_DIR: Final[str] = "02.Data-Structures-And-Algorithms-In-Python-Book"
##################################################################################################

# Get file arguments
SUBFOLDER: Final[str] = argv[1]
FILENAME: Final[str] = argv[2]
opts: dict[str, bool] = {
    "nomypy": False,
    "keepcells": False,
    "keepmd": False,
    "noformat": False,
}
for k in opts:
    if f"--{k}" in argv:
        opts[k] = True

# Path variables
CURRENT_PATH: Final[str] = path.abspath(__file__)  # Absolute path
CURRENT_DIR_ABS: Final[Path] = Path(__file__).parent.resolve()  # Absolute Path
CURRENT_DIR: Final[str] = path.basename(CURRENT_DIR_ABS)  # Dirname only


# HELPER FUNCTION
# ---------------
def convert_ipynb_to_py(
    notebook_path: Path, module_path: Path, options: dict[str, bool]
) -> None:
    """Convert a .ipynb file to .py."""

    exporter_configs: dict[str, Any] = {
        "TemplateExporter": {"exclude_markdown": not options["keepmd"]}
    }

    print()
    print("Converting:")
    print(f"Source: {notebook_path}")
    print(f"Target: {module_path}")

    with open(notebook_path, encoding="utf-8") as f:
        nb = nbformat.reads(f.read(), nbformat.NO_CONVERT)

    exporter = PythonExporter(exporter_configs)
    source, _ = exporter.from_notebook_node(nb)

    with open(module_path, "w", encoding="utf-8") as f:
        f.writelines(source)

    # If opts["keepcells"] is not set, cleanup the notebook cells in the final .py file
    if not opts["keepcells"]:
        with open(module_path, "r+", encoding="utf-8") as f:
            py_contents = f.read()
            py_contents = re.sub(r"#\sIn\[\d*\s*]:\s*\n*", "", py_contents)

            # If opts["noformat"] is true, skip formatting
            # Assume black is installed
            if not opts["noformat"]:
                py_contents = black.format_str(py_contents, mode=black.FileMode())

            f.seek(0)
            f.write(py_contents)
            f.truncate()

    print()
    print("Conversion Complete")
    print()

    # If opts["nomypy"] is true, skip mypy setup
    if not opts["nomypy"]:
        mypy_result = mypy.api.run(
            ["--strict", "--ignore-missing-imports", str(module_path)]
        )

        if mypy_result[0]:
            print("\nMypy Type checking report:\n")
            print(mypy_result[0])  # stdout

        if mypy_result[1]:
            print("\nMypy Error report:\n")
            print(mypy_result[1])  # stderr

        print("Mypy Exit status:", mypy_result[2])


# Early exit if script is not executed from the project folder
try:
    if CURRENT_DIR != PROJ_DIR:
        # Wrong directory for execution: Error and abort
        error_msg = "Error - Wrong Directory:\n"
        error_msg += (
            f"Only execute this script from the '{PROJ_DIR}' project root-directory.\n"
        )
        error_msg += "Aborting..."
        raise ValueError(error_msg)
except ValueError as err:
    print("-" * 106)
    print(err)
    print("-" * 106)
    sysexit(1)

# Build $IPYNB_FILE_PATH
SUBFOLDER_PATH = Path(path.join(CURRENT_DIR_ABS, SUBFOLDER)).resolve()
IPYNB_FILE_PATH = Path(path.join(SUBFOLDER_PATH, f"{FILENAME}.ipynb")).resolve()
PY_FILE_PATH = Path(path.join(SUBFOLDER_PATH, f"{FILENAME}.py")).resolve()

# print(SUBFOLDER_PATH)
# print(IPYNB_FILE_PATH)

# Early exit if IPYNB_FILE_PATH does not exist
if not path.exists(IPYNB_FILE_PATH):
    # The specified subfolder does not exist: Error and abort
    try:
        error_msg = "Error - Subfolder or file does not exist:\n"
        error_msg += f"The specified subfolder '{SUBFOLDER}' or file '{FILENAME}' does not exist.\n"
        error_msg += "Aborting..."
        raise ValueError(error_msg)
    except ValueError as err:
        print("-" * 106)
        print(err)
        print("-" * 106)
        sysexit(1)


convert_ipynb_to_py(IPYNB_FILE_PATH, PY_FILE_PATH, opts)
