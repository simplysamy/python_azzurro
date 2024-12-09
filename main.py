z = 30  # Global variable

def my_function():
    global z  # Declare z as global to modify it
    z = 40   # Modify the global variable
    print("Inside the function, z =", z)

my_function()  # Modify and print z
print("Outside the function, z =", z)  # Accessing the modified global variable
