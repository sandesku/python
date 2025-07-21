# Before performing operations on a file, it's often useful to check if the file exists.
# You can do this using the os.path.exists() function.

import os

filename = "example.txt"

# Check if the file exists
if os.path.exists(filename):
    print(f"{filename} exists.")
else:
    print(f"{filename} does not exist.")