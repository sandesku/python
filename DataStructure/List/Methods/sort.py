# The sort() method sorts the elements of the list in ascending order by default.
# You can also sort in descending order by specifying reverse=True.

numbers = [3, 1, 4, 1, 5, 9]
numbers.sort()
print(numbers)  # Output: [1, 1, 3, 4, 5, 9]

numbers.sort(reverse=True)
print(numbers)  # Output: [9, 5, 4, 3, 1, 1]