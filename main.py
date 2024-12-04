user_input = input("Enter a number: ")

try:
    number = float(user_input)
    print(number)
    
except Exception as e:
    print(e)