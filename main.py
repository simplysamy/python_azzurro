def greeter(*args): # do not know how many arguments will be supplied when a function is called. 
   for name in args:
      print('Welcome', name)

greeter('John', 'Denise', 'Phoebe', 'Adam', 'Gryff', 'Jasmine')