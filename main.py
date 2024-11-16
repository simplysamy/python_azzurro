users = {'user1':'mario123',
         'user2':'luigi123,'}

# user1 = users['user1'] # throws an error if user1 does not exist

user1 = users.get('user3') ## does not throw an error 

print(user1)