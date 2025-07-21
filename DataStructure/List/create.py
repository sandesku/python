# List of integers
numbers = [1, 2, 3, 4, 5]

print(type(numbers))
print("numbers : ", numbers)


# List of strings
fruits = ["apple", "banana", "cherry"]

# Mixed data types
mixed_list = [1, "hello", 3.14, True,1,"hello",3.14,False,"Arul"]
print("Length of the list",len(mixed_list))
print("Last Index", len(mixed_list)-1)
print(mixed_list[0]) # 1
print(mixed_list[1]) # hello
print(mixed_list[2]) # 3.14
print(mixed_list[3]) # True
print(mixed_list[8]) # Arul

# access the last index using -1
print("Count from reverse")
print(mixed_list[-1])
print(mixed_list[-2])
print(mixed_list[-3])
print(mixed_list[-4])
print(mixed_list[-5])

# Empty list
empty_list = []
print(empty_list[0])