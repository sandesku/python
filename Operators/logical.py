a = 5
b = 10
c = 15

# Using and
if c < a < b:
# 5 > 15 -- false
# 10 > 5 -- true
# if false and true : -- false
    print("Both conditions are True")

# Using or
if a > c or b > a:
# 5 > 15 -- false
# 10 > 5 -- true
# if false or true : -- true
    print("At least one condition is True")

if not (a > c):
# 5 > 15 -- false -- not(false) -- true
    print("Checking Not expression")