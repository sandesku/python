# To move a file from one location to another, you can use the shutil.move() function.
# This will also rename the file if the destination has a different name.
import os
import shutil

source = "copy_of_sample.txt"
destination = "my_folder/copy_of_sample.txt"

# Move the file
if not os.path.exists("my_folder"):
    os.mkdir("my_folder")

shutil.move(source, destination)
print(f"Moved {source} to {destination}.")