items: set = {'apple', 'banana', 10, True}

#items.remove(100) # of iterm doesn't exist, it will throw an error

items.discard(100) # of iterm doesn't exist, it will not throw an error
print(items)