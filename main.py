def outer_function():
    x = 10
    
    def inner_function():
        x = 5  # This creates a new local variable x in inner_function
        print("Inner function, x =", x)
    
    inner_function()
    print("Outer function, x =", x)

outer_function()