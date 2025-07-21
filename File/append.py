# If you want to add more content to an existing file, you can open the file in 'a' (append) mode.
# Here’s an example:

filename = "example.txt"

# Appending to a file
with open(filename, "a") as file:
    file.write("Appending another line to the file.\n")

# Reading the updated file content
with open(filename, "r") as file:
    updated_content = file.read()

print("Updated content of the file:")
print(updated_content)