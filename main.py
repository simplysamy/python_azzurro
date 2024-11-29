def do_something(n: int):
    print(n)
    
    if n==1:
        print("done with the function")
        return
    
    do_something(n-1) # recursive call - function calls itself
    
do_something(3)
    