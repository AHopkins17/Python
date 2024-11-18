# Custom exception Creation
# Define custom exception class
class NotNumericError(Exception):
    """Exception raised when input is not a numeric value.""" 
    def __init__(self, input_value, message="is not a number."):
        self.input_value = input_value
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return f"{self.input_value} {self.message}"

# Main function   
def main():
    while True:
        try:
            # Prompt for user input and validate
            user_input = input("Please enter a number: ")

            # isnumeric
            if not user_input.isnumeric():
                raise NotNumericError(user_input)
        # Handle invalid input
        except NotNumericError as error:
            print(f"Error: {error} ")
        # Confirm valid input
        else:
            print(f"You entered a valid number: {user_input}")
            break
            
        finally:
            # Indicate end of this iteration
            print("End of input program.\n")

# Run main function
if __name__ == "__main__":
    main()