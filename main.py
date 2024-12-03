def do_something(*args, **kwargs):
    print(args)  # Tuple
    print(kwargs) # DIctionary
    
do_something("hello", name='Sam', age=10) 