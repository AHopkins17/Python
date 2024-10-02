# Number Guessing Game

import random

def main():
    # Generate random number between 1 and 100
    actual_number = random.randint(1, 100)

    print("Welcome to the Number Guessing Game!")
    print("I have selected a random number between 1 and 100. Try to guess it!")

    while True:
        try:
            # User guess entry
            guess = int(input("Enter your guess: "))

            # Absolute difference
            difference = abs(guess - actual_number)
            
            # Feedback based on the difference
            if difference == 0:
                print(f"Alright! You guessed the correct number: {actual_number}")
                break
            elif difference <= 5:
                print("Very Hot")
            elif difference <= 15:
                print("Hot")
            elif difference <= 25:
                print("Cool")
            else:
                print("cold")

        except ValueError:
            print("Please enter a valid integer.")
if __name__ == "__main__":
    main()