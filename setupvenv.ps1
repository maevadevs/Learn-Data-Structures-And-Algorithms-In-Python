#############################################################################################
# FILE: setupvenv.ps1                                                                       #
# PROJECT: Standalone Script                                                                #
# PURPOSE: This Script automates the following for a Python project:                        #
#   1. Ensure the correct version of Python is used for the project                         #
#   2. Create a Virtual Enviroment for the project (skip if venv folder exists)             #
#   3. Activate venv                                                                        #
#   4. Install/Upgrade base modules in venv: pip, setuptools, safety                        #
#   5. Install/upgrade dependencies in the venv from scratch or from requirements.txt       #
#   6. Export the requirements.txt                                                          #
#   7. Run safety and audit checks on dependencies                                          #
#   8. Deactivate venv and return to powershell prompt                                      #
# BEFORE RUNNING: Make sure to define the following variables below:                        #
#   - $PROJ_DIR: The name of the root project folder                                        #
#   - $PROJ_DEPENDENCIES: List of all dependencies for the python project in string format  #
#   - $PROJ_PY_VERSION: The Python version to use for this project                          #
# PARAMETERS: NONE                                                                          #
# EXAMPLE CALL:                                                                             #
#   - Make sure to call this script from the project root directory from Powershell:        #
#       > ./setupvenv.ps1                                                                   #
# NOTE: To upgrade to latest dependencies:                                                  #	
#	1. Delete the requirements.txt file                                                     #
#	2. Delete the venv folder                                                               #
#	3. Re-run this script                                                                   #
#############################################################################################
# 1.0.0     2022/06/30      Maeva Ralafiarindaza    : INITIAL RELEASE                       #
# 1.1.0     2023/03/15      Maeva Ralafiarindaza    : Additional improvements & conditions  #
#############################################################################################
# ACTION ITEM: Input the name of the project folder
$PROJ_DIR = "02.Data-Structures-And-Algorithms-In-Python-Book"
# ACTION ITEM: List the dependencies for the project in this variable
$PROJ_DEPENDENCIES = "jupyterlab jupyter_contrib_nbextensions jupyterthemes mypy black"
# ACTION ITEM: Add the supported version of Python
$PROJ_PY_VERSION = "3.11"
# ACTION ITEM: Call this script from the project folder: > ./setupvenv.ps1 
#############################################################################################

# Path variables
$CURRENT_PATH = Get-Location
$CURRENT_DIR = Split-Path -Path (Get-Location) -Leaf
# Base dependencies
$BASE_MODULES = "pip setuptools pip-audit"
# Python version
$PROJ_PY_VERSIONS = $PROJ_PY_VERSION.Split(".")
$PROJ_PY_MAJ = $PROJ_PY_VERSIONS[0]
$PROJ_PY_MIN = $PROJ_PY_VERSIONS[1]
$SYS_PY_VERSION = (Get-Command python).Version.ToString()
$SYS_PY_VERSIONS = $SYS_PY_VERSION.Split(".")
$SYS_PY_MAJ = $SYS_PY_VERSIONS[0]
$SYS_PY_MIN = $SYS_PY_VERSIONS[1]

# Early exit if installed Python does not match the project's supported version
if (($PROJ_PY_MAJ -ne $SYS_PY_MAJ) -or ($PROJ_PY_MIN -ne $SYS_PY_MIN))
{
    # Wrong directory for execution: Error and abort
    Write-Host "-----"
    Throw "Error - Wrong Python Version: Your Python version is not supported. Project requires Python $($PROJ_PY_VERSION) but you have Python $($SYS_PY_VERSION). Aborting..."
}

# Early exit if script is not executed from the project folder
if ($CURRENT_DIR -ne $PROJ_DIR) 
{
    # Wrong directory for execution: Error and abort
    Write-Host "-----"
    Throw "Error - Wrong Directory: Please only execute this script from the `"$($PROJ_DIR)`" project root-directory. Aborting..."
}

Write-Host ""
Write-Host "Executing script from $($CURRENT_PATH)..."

# Check if a venv folder already exist
if (Test-Path "$($CURRENT_PATH)\venv") 
{
    # Display warning message
    Write-Host ""
    Write-Host "----- A venv folder already exist: Activating venv -----"
    Write-Host ""
} 
else 
{
    # Create a new virtual enviroment
    Write-Host ""
    Write-Host "----- Creating & Activating Virtual Env -----"
    Write-Host ""
    python -m venv .\venv
}

# Activate venv
.\venv\Scripts\Activate.ps1
# Upgrade base modules in venv
Write-Host ""
Write-Host "----- Installing/Upgrading base modules in Virtual Env -----"
Write-Host ""
Start-Process -NoNewWindow -Wait -FilePath ".\venv\Scripts\python.exe" -ArgumentList "-m pip install --upgrade $($BASE_MODULES)"

# Install/Update dependencies in venv: Check if requirements.txt already exist
if (Test-Path -Path .\requirements.txt -PathType Leaf) 
{
    Write-Host ""
    Write-Host "----- requirements.txt found. Installing/Upgrading from requirements.txt -----"
    Write-Host ""
    # Install from predefined requirements
    python -m pip install -r .\requirements.txt
}
else 
{
    Write-Host ""
    Write-Host "----- requirements.txt not found. Installing from scratch -----"
    Write-Host ""
    # Install from scratch 
    Start-Process -NoNewWindow -Wait -FilePath ".\venv\Scripts\python.exe" -ArgumentList "-m pip install --upgrade $($PROJ_DEPENDENCIES)"
    # python -m pip install --upgrade $dependencies_list
    # Export the requirements.txt
    python -m pip freeze > requirements.txt
}

# Run safety checks on installed dependencies
Write-Host ""
Write-Host "----- Running safety and audit checks on dependencies -----"
Write-Host ""
pip-audit

# Setup settings for Jupyter Themes
Write-Host ""
Write-Host "----- Setup settings for Jupyter Themes -----"
Write-Host ""
jt -t onedork -fs 12 -nfs 12 -tfs 12 -dfs 11 -ofs 11 -T -N -kl 

# Deactivate venv
Write-Host ""
Write-Host "----- All setup completed. Now deactivating env -----"
Write-Host ""
deactivate