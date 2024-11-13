people: list = ['Mario', 'Luigi', 'peach', 'toad']
people2: list[str] = ['sonic', 'tails']

# List can also be defined as below
    # people = ['Mario', 'Luigi', 'peach', 'toad']  
    # people: list[str] = ['Mario', 'Luigi', 'peach', 'toad']
    
print(people)

# lenght of the list
print(len(people))

#print the first element of the list
print(people[0])

# negetive index
print(people[-1])

# range of the list
print(people[0:2])

# last two elements
print(people[-2:])  # form index number -2 till end of the list towards right
print(people[2:])   # form index number 2 till end of the list

# check if an element is in the list
# case sensitive
print('peach' in people)  # (Peach with capital P is not in the list)

# add new element to the list
people[0] = 'sam'

print(people)

people[0:2] = ['sam', 'hasan']
print(people)

#insert an element in the list
people.insert(2, '!!!')
print(people)

# append to a list 
people.append('york')
print(people)

# adding one list to another
people.extend(people2)
print(people)

people += people2
print(people)

# adding one list to another with new variable
new_list = people + people2
print(new_list)
