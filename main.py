items1: set = {'apple', 'banana', 10, True}
items2: set = {'apple', 10, False, 14}
items1.symmetric_difference_update(items2) # Updates the current set
print(items1)

new_set =items1.symmetric_difference(items2) # Updates the current set & provide the output in the new set
print(new_set)