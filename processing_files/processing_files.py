# Define main fucntion
def main():
    total = 0.0
    count = 0
    try:
        # Open the file in read mode
        with open('processing_files/sales_totals.txt', 'r') as file:
            # Read each line using readline() in a loop
            while True:
                line = file.readline()
                if not line:  # Break the loop if end of file is reached
                    break
                try:
                    # Strip newline and convert to float
                    number = float(line.strip())
                    # Add to running total
                    total += number
                    # Increment the count
                    count += 1
                    # Format and display number
                    print(f"{number:,.2f}")
                except ValueError:
                    print(f"Skipping invalid line: {line}")
        
        # Outside of loop, calculate and display the total, count, and average
        if count > 0:
            average = total / count
            print(f"Total: {total:,.2f}")
            print(f"Number of entries: {count}")
            print(f"Average: {average:,.2f}")
        else:
            print("No valid data to process.")
    
    except FileNotFoundError:
        print("Error: The file 'sales_totals.txt' was not found.")
    except IOError:
        print("Error: There was an issue reading the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call main function
if __name__ == "__main__":
    main()