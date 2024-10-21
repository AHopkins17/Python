def main():
    # User Input
    user_input = input("Enter a character: ")

    # Validate Input
    while len(user_input) != 1:
        print("Please enter exactly one character.")
        user_input = input("Enter a charater: ")

        # Convert to ASCII Value
        ascii_value = ord(user_input)

        # Result
        print(f"The ASCII value of '{user_input}' is {ascii_value}")

# Call the main function
if __name__ == "__main__":
    main()