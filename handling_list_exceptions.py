# Starting Program

def main():
    top_artists = [
        "The Beatles", 
        "Madonna", 
        "Elton John", 
        "Elvis Presley", 
        "Mariah Carey", 
        "Stevie Wonder", 
        "Janet Jackson", 
        "Michael Jackson", 
        "Whitney Houston", 
        "Rihanna"
    ]

    print("Current Top Artists:")
    print(top_artists)

    # Replace artist in list
    def replace_artist():
        try:
            # Index from user
            index = int(input("Enter the index of the artist to replace (0-9): "))

            # New artist name
            new_artist = input("Enter the new artist name: ")
            
            # Replace artist
            top_artists[index] = new_artist
            print("Updated list:", top_artists)

        except (ValueError, IndexError):
            print("An input error occurred. Please ensure you enter a valid index and artist name.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    # Call the function to replace an artist
    replace_artist()

# Call the main function
if __name__ == "__main__":
    main()