# To write to a file, you can use the open() function in Python, specifying the file mode as 'w' for writing.
# Here's an example:

# Writing to a file
filename = "example.txt"

with open(filename, "w") as file:
    file.write("Hello, this is a sample text file.\n")
    file.write("Google Colab makes file handling easy!\n")

print(f"{filename} has been created and written to.")