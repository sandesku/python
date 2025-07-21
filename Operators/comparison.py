print(5 == 5)  # True
print(5 == 6)  # False

print(5 != 5)  # False
print(5 != 6)  # True

print(5 > 6)   # False
print(6 < 5)   # False

print(6 <= 6)   # True
print(5 >= 4)   # True

age = int(input("Enter your age : "))

if age >= 18:
  print("You are an adult")
else:
  print("You are not an adult")