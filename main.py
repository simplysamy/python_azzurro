user_input: str = input("Enter a number: ")

if user_input == '0':
    raise Exception("Please don't enter 0")