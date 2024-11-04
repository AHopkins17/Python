
def is_between_8_and_20(password):
    length_of_password = len(password)
    if length_of_password<8 or length_of_password>20:
        return False
    else:
        return True
    
def has_one_uppercase(password):
    for char in password:
        if char.isupper():
            return True
    return False

def has_one_lowercase(password):
    for char in password:
        if char.islower():
            return True
    return False

def has_one_number(password):
    for char in password:
        if char.isdigit():
            return True
    return False

def has_one_symbol(password):
    symbols = "!@#$%*"
    for char in password:
        if char in symbols:
            return True
    return False
    
def main():
    """
    1. [X] Set up your program in a main() function
    2. {X] Create a Python program that asks the user to input a password.
    3. Ensure the password meets the following criteria:
        [X] Between 8 to 20 characters long.
        [X] Contains at least one uppercase letter.
        [X] Contains at least one lowercase letter.
        [X] Includes at least one number.
        [X] Includes at least one symbol from the set: !@#$%&*.
    4. [X] Use a while loop to keep asking for the password until all criteria are met.
    5. [X] Once a valid password is entered, prompt the user to enter it again for      confirmation.
    6. [X] Use try-except blocks to handle any errors or exceptions that occur.
    7. [X] If the second password entry matches the first, display a success message.    Otherwise, prompt the user to start the process again.
    """
    while True:
        try:    
            user_input = input("Enter a password: ")
            length = is_between_8_and_20(user_input)
            upper = has_one_uppercase(user_input)
            lower = has_one_lowercase(user_input)
            number = has_one_number(user_input)
            symbol = has_one_symbol(user_input)

            if length and upper and lower and number and symbol:
                confirmation = input("Please confirm your password: ")

                if confirmation == user_input:
                    print("Password successfully created!")
                    break
                else:
                    print("Passwords do not match. Please try again.")
            else:
                print("Doesnt meet criteria. Please make sure it:")
                if not length:
                    print("- Is between 8 to 20 characters long.")
                if not upper:
                    print("- Contains at least one uppercase letter.")
                if not lower:
                    print("- Contains at least one lowercase letter.")
                if not number:
                    print("- Includes at least one number.")
                if not symbol:
                    print("- Includes at least one symbol from the set: !@#$%&*")

        except Exception as e:
            print(f"An error occured: {e}")

if __name__ == "__main__":    
    main()