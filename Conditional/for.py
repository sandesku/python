# The for loop is used to iterate over a sequence (such as a list, tuple, dictionary, set, or string) or a range of numbers.

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


for i in range(1, 6):
    print("Iteration", i)


for i in range(1, 11):
    if i == 5:
        break
    print(i)