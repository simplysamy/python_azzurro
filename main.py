def do_something(**kwargs):
    print(kwargs)
    
    print(kwargs['name'])
    

do_something(name='Sam', age=10) # Key words arguments are basically key value pairs