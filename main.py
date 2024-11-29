def square(n):
  return n * n

print(square(2))

# Store result from square in a variable
result = square(4)
print(result)

# Send the result from square immediately to another function
print(square(5))

# Use the result returned from square in a conditional expression
if square(3) < 15:
    print(f'{square(3)} is less than 15')