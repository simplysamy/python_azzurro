user_input = input("Enter a number: ")

try:
    number = float(user_input)
    print(number)
    
except ValueError:
    print("Invalid input. Please enter a valid number.")