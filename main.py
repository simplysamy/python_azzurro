def outer_function():
    x = 10  # Variable in outer function's scope
    
    def inner_function():
        nonlocal x  # Indicates that we want to use the x in the outer_function
        x += 5  # Modify the outer function's variable
        print("Inner function, x =", x)
    
    inner_function()  # Call inner_function
    print("Outer function, x =", x)  # Check the value of x in the outer function

outer_function()