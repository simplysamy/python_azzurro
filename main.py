items1: set = {'apple', 'banana', 10, True}
items2: set = {'apple', 10, False, 14}

items1.symmetric_difference_update(items2)
print(items1)