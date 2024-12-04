user_input = input("Enter a number: ")

try:
    number = float(user_input)
    result = number / 0
    print(number)
    
except ValueError:
    print("Invalid input. Please enter a valid number.")
    
except ZeroDivisionError:
    print("Please don't divide by zero!")
    
except Exception as e:
    print(f"An error occurred: {e}")