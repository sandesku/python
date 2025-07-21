# To delete a file, you can use the os.remove() function.
# Be careful with this operation as it will permanently remove the file.

import os

filename = "example.txt"

# Delete the file
if os.path.exists(filename):
    os.remove(filename)
    print(f"{filename} has been deleted.")
else:
    print(f"{filename} does not exist.")