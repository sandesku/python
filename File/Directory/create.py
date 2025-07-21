# To create a new directory (folder), you can use the os.mkdir() function.
# This is useful for organizing files into different folders.
import os

# Create a new directory
new_dir = "my_folder"

if not os.path.exists(new_dir):
    os.mkdir(new_dir)
    print(f"Directory {new_dir} created.")
else:
    print(f"Directory {new_dir} already exists.")