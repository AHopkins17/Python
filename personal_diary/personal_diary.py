# Define main fuction
def main():
    # Ask user for date and time
    date_time = input("Enter today's date (MM-DD-YYYY) and time (HH:MM): ")
    diary_entry = input("Enter diary entry: ")

    # Open file in append mode and add entry without overwrite
    file = open('diary.txt', 'a')

    # Write date, time, and diary entry to file
    file.write(f"Date and Time: {date_time}\n")
    file.write(f"Diary Entry: {diary_entry}\n")

    # Blank line
    file.write("\n")

    # Close file
    file.close()

    # Tell user their entry is saved
    print("Your diary entry has been saved.")

# Call main function
if __name__ == "__main__":
    main()
    