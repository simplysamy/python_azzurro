def greeter(name: str,
            title: str = 'Dr',
            prompt: str = 'Welcome',
            message: str = 'Live Long and Prosper'):
    print(prompt, title, name, '-', message)
    
greeter ('john')

greeter('sam', prompt='Hi', title='Mr') # Named parameters - Order does not matter