# To remove a directory, you can use the os.rmdir() function.
# Note that the directory must be empty before it can be removed.
import os

new_dir = "my_folder"

# Remove a directory
if os.path.exists(new_dir):
    os.rmdir(new_dir)
    print(f"Directory {new_dir} has been removed.")
else:
    print(f"Directory {new_dir} does not exist.")