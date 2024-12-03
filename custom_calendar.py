# Custom Calendar
import calendar 
from datetime import datetime

def main():
    try:
        # Get the current year
        current_year = datetime.now().year

        # Ask the user for their birth month
        birth_month = input("Enter your birth month (as a number. 5 for May): ")

        # Validate the user input
        if not birth_month.isdigit() or not (1 <= int(birth_month) <= 12):
            print("Invalid input! Please enter a number between 1 and 12.")
            return main()

        # Convert validated input to integer
        birth_month = int(birth_month)

        # Generate and display calendar
        print(f"\nHere is the calendar for your birth month in {current_year}:\n")
        print(calendar.month(current_year, birth_month))

    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}")
        main()

# Run program
if __name__ == "__main__":
    main()