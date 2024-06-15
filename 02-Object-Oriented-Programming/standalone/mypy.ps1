###
# Run this file by itself to run mypy on all source files in this folder
###

# Run mypy on all .py files in the current directory
python -m mypy --strict .

# After all is done, delete the .mypy_cache folder
Remove-Item .mypy_cache -Recurse