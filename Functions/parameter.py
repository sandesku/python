# Functions can accept multiple parameters and return values.
# Parameters are used to pass information to the function,
# and the return statement is used to send a result back to the caller.

# Defining a Function with Multiple Parameters

def add_numbers(a, b):
    """Returns the sum of two numbers."""
    return a + b

# Calling the Function
result = add_numbers(5, 3)
print(f"Sum: {result}")

# Defining a Function Without Parameters

def say_hello():
    """Prints a hello message."""
    print("Hello, World!")

# Calling the Function
say_hello()

# Defining a Function with Default Parameters

def greet(name="Guest"):
    """Prints a greeting message with a default name."""
    print(f"Hello, {name}!")

# Calling the Function
greet()
greet("Bob")