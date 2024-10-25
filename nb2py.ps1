############################################################################################################
# FILE: nb2py.ps1
# PROJECT: Standalone Script
# PURPOSE: This script automates the following for a Python project:
#   1. Convert a .ipynb file into .py
#   2. Ensure that .py files are using static types correctly using mypy (Optional)
#   3. Keep or remove the jupyter notebook cells in the .py file (Optional)
#   4. Keep or remove the jupyter notebook markdown (comments) in the .py file (Optional)
# PARAMETERS:
#   1. Subfolder that contains the .ipynb file o convert (required)
#   2. Filename of the .ipynb file without the extension (required)
#   3. We are using mypy by default. To skip mypy check, set -nomypy
#   4. Jupyter notebook cells are removed by default. To keep the cells, set -keepcells
#   5. Formatting using Black is applied by default. To skip formatting, set -noformat
# EXAMPLE CALL:
#   - Make sure to call this script from the project root directory from Powershell:
#       > .\nb2py notes notebook *> log.txt
#       > .\nb2py not* not* -nompypy
#       > .\nb2py not* not* nomypy -keepcells -keepmd -noformat
############################################################################################################
#   1.0.0   2023-03-15      Maeva Ralafiarindaza    :   INITIAL RELEASE
#   1.1.0   2023-03-25      Maeva Ralafiarindaza    :   Allow wildcard * in args and resolve
#                                                       Add -nomypy, -keepcells, and -keepmd optional params
#   1.2.0   2023-04-21      Maeva Ralafiarindaza    :   Add -noformat optional params
#   2.0.0   2023-05-29      Maeva Ralafiarindaza    :   Convert to setup for Anaconda
############################################################################################################
# File Parameters
param (
    [Parameter(Mandatory = $True)] [String] $subfolder,
    [Parameter(Mandatory = $True)] [String] $file,
    [switch] $nomypy = $False,
    [switch] $keepcells = $False,
    [switch] $keepmd = $False,
    [switch] $noformat = $False
)
############################################################################################################
# ACTION ITEM: Input the nae of the project folder
$PROJ_DIR = "02.Data-Structures-And-Algorithms-In-Python-Book"
############################################################################################################

# Path variables
$CURRENT_PATH = Get-Location
$CURRENT_DIR = Split-Path -Path (Get-Location) -Leaf

# Early exit if script is not executed from the project folder
if ($CURRENT_DIR -ne $PROJ_DIR) {
    # Wrong directory for execution: Error and abort
    Write-Host "-----"
    Throw "Error - Wrong Directory: Only execute this script from the `"$($PROJ_DIR)`" project root-directory. Aborting..."
}

# Build $IPYNB_FILE_PATH
$SUBFOLDER_PATH = Resolve-Path -Path (Join-Path -Path $CURRENT_PATH -ChildPath $subfolder)
$IPYNB_FILE_PATH = Resolve-Path -Path (Join-Path -Path $SUBFOLDER_PATH -ChildPath $($file + '.ipynb'))

# Early exit if IPYNB_FILE_PATH does not exist
if (-not (Test-Path -Path $IPYNB_FILE_PATH)) {
    # The specified subfolder does not exist: Error and abort
    Write-Host "-----"
    Throw "Error: The specified subfolder `"$($subfolder)`" or file `"$($file)`" does not exist. Aborting..."
}

# If $IPYNB_FILE_PATH is valid, run build command
# If $nomypy is true, skip mypy setup
# Not applicable with Conda: Simply expect installation ready or fail on calls
# if (-not $nomypy) {
#     # Install mypy if it is not installed already
#     $MYPY_PATH = Join-Path -Path $CURRENT_PATH -ChildPath "venv" | Join-Path -ChildPath "Lib" | Join-Path -ChildPath "site-packages" | Join-Path -ChildPath "mypy"
#     if (-not (Test-Path -Path $MYPY_PATH)) {
#         Start-Process -NoNewWindow -Wait -FilePath ".\venv\Scripts\python.exe" -ArgumentList "-m pip install mypy"
#     }
# }

# Convert .ipynb to .py with jupyter notebook
Start-Process -NoNewWindow -Wait -FilePath "python" -ArgumentList "-m jupyter nbconvert --to python $($IPYNB_FILE_PATH) --PythonExporter.exclude_markdown=$(-not $keepmd)"

# If -keepcells is not set, cleanup the notebook cells in the final .py file
if (-not $keepcells) {
    $PY_FILE_PATH = Resolve-Path -Path (Join-Path -Path $SUBFOLDER_PATH -ChildPath $($file + '.py'))
    $py_contents = Get-Content -Path $($PY_FILE_PATH) -Raw
    $py_contents = $py_contents -Replace '#\sIn\[\d*\s*]:\s*\n*', ''
    $py_contents | Set-Content -Path $($PY_FILE_PATH)
}

# If -noformat is true, skip formatting
# Assume black is installed
if (-not $noformat) {
    # Resolve the path of the .py file
    $PY_FILE_PATH = Resolve-Path -Path (Join-Path -Path $SUBFOLDER_PATH -ChildPath $($file + '.py'))

    # Format the exported file using black
    Start-Process -NoNewWindow -Wait -FilePath "python" -ArgumentList "-m black $($PY_FILE_PATH)"
}

# If -nomypy is true, skip mypy setup
# Assume mypy is installed
if (-not $nomypy) {
    # Resolve the path of the .py file
    $PY_FILE_PATH = Resolve-Path -Path (Join-Path -Path $SUBFOLDER_PATH -ChildPath $($file + '.py'))

    # Static types checking with mypy
    # This only checks types conformance during build time, not at runtime
    Start-Process -NoNewWindow -Wait -FilePath "python" -ArgumentList "-m mypy --strict $($PY_FILE_PATH)"
}
