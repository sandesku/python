# To list all files and directories in a specified directory, you can use os.listdir().

import os

# List files in a directory
directory = "."
files = os.listdir(directory)

print(f"Files in {directory}:")
for file in files:
    print(file)