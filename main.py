a = 0.1 + 0.2  # Result is slightly more than 0.3
b = 0.3
epsilon = 1e-17  # Set a small tolerance level

# Standard comparison
print(a == b)  # This will output False

# Using tolerance level
if abs(a - b) < epsilon:
    print("a is approximately equal to b")
else:
    print("a is not equal to b")  # This will be printed