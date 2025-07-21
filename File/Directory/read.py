# Sometimes, you may want to read a file line by line instead of reading the entire content at once.
# This can be done using a loop.

# Writing sample content to a file
with open("sample.txt", "w") as file:
    file.write("First line\nSecond line\nThird line\n")

# Reading the file line by line
with open("sample.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() is used to remove the newline character