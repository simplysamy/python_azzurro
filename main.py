price1 = 19.99
price2 = 19.99 + 0.0000000001  # Slightly more than 19.99
epsilon = 1e-10  # Set a very tight tolerance level

if abs(price1 - price2) < epsilon:
    print("Prices are approximately equal")  # This will be printed
else:
    print("Prices are not equal")