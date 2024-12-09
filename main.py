def outer_function():
    count = 0  # A variable to keep track of counts
    
    def inner_function():
        nonlocal count  # Indicating we will modify count in the outer_function
        count += 1  # Increment the count
        print("Count in inner function:", count)

    inner_function()  # Call it a few times
    inner_function()
    inner_function()

outer_function()