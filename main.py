user_input: str = input('You: ')

try:
    number = float(user_input)
    print(number)

except Exception as e:
    print('Exception: ', e)
    
# If the above program runs into NO_Error then this block will run
else: 
    print("Successfully Executed the code")