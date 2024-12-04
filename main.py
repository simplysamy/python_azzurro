def do_math():
    user_input = input("Enter a number: ")

    try:
        number = float(user_input)
        print(number)
        
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        
        do_math() # recursion
        
        
    except Exception as e:
        print(f"An error occurred: {e}")

do_math()