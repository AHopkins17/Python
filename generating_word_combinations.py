# Define generator function
def two_letter_combinations(characters):

# Outer loop iterates over each characters
    for char1 in characters:
        # Inner loop iteratres to form pairs
        for char2 in characters:
            yield char1 + char2

# Define main
def main():
    # Create list of 5 unique characters
    characters = ['q', 'r', 's', 't', 'u']

    # Call generator function and print combinations
    print("Two-letter combinations:")

    # Using loop to iterate over generators output
    for combination in two_letter_combinations(characters):
        print(combination)

# Call the function
main()
