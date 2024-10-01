# Calculating Factorials

def factorial(n):
    # Base case: the factorial of 0 or 1 is 1
    if n == 0 or n ==1:
        return 1
    # Recursive case: n multiplied by the factorial of (n-1)
    else:
        return n * factorial(n-1)

def main():
    # Ask user to enter a non-negative integer;
    user_input = input("Enter a non-negative integer: ")

    # Convert user input to an integer
    n = int(user_input)

    # Check if entered number is non-negative
    if n < 0:
        print("Please enter a non-negative integer.")
    else:
        # Call the factorial function and keep results
        result = factorial(n)
        # Print results in formatted string
        print(f"The factorial of {n} is {result}.")
    
# Calling main function
if __name__ == "__main__":
    main()