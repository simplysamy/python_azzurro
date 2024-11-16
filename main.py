items: set = {'apple', 'banana', 10, True}

items.add('orange')  # add an item to the set

print(items)

items.update(['carrots', 15]) # it can be a list

# items.update({'carrots', 15}) it can be a set

# items.update(('carrots', 15))  it can be a tuple

print(items)