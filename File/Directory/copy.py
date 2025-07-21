# To copy a file from one location to another, you can use the shutil module.

import shutil

source = "sample.txt"
destination = "copy_of_sample.txt"

# Copy the file
shutil.copy(source, destination)
print(f"Copied {source} to {destination}.")