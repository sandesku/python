# You can rename a file using the os.rename() function.
# This is useful if you want to change the name of an existing file.

import os

old_filename = "example.txt"
new_filename = "renamed_example.txt"

# Rename the file
if os.path.exists(old_filename):
    os.rename(old_filename, new_filename)
    print(f"{old_filename} has been renamed to {new_filename}.")
else:
    print(f"{old_filename} does not exist.")
