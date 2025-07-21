# To read from a file, you can use the open() function with the mode 'r' for reading.
# Here's how you can read the contents of the file we just created:

filename = "example.txt"

# Reading from a file
with open(filename, "r") as file:
    content = file.read()

print("Content of the file:")
print(content)