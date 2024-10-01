# Simple Python program to calculate the square of a number

def square_number():
    while True:     # Loop until valid number entered
        try:
            number = input("Enter a number to square: ")
            squared_number = int(number) ** 2   # Convert input to integar and calculate the square
            print(f"The square of {number} is {squared_number}.")
            break   #Exit loop if conversion and calculation successful
        except ValueError: # Handle the case where input cannot be converted
            print("Invalid input. Please enter a numeric value.")

# Call to function
square_number()