users = {'user1':'mario123',
         'user2':'luigi123',
         'items': {'apple': 10, 
                   'banana': 5}}   # dictionary inside a dictionary
 

print(users.setdefault('user1', 'There is no key'))

print(users.setdefault('sam', 'There is no key'))