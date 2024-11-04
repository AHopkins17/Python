def main():
    # Empty list to store flower names
    flowers = []
    
    # User Input
    print("Enter names of flowers (type 'done' when finished):")
    
    while True:
        flower = input("Flower name: ")
        if flower.lower() == "done":
            break
        else:
            flowers.append(flower)
    
    # Sort list of flowers
    flowers.sort()
    
    # Print sorted flower list with numbering
    print("\nSorted List of Flowers:")
    for index, flower in enumerate(flowers, start=1):
        print(f"{index}. {flower}")
    
    # Search for specific flower
    search_flower = input("\nEnter the name of a flower to search for: ")
    if search_flower in flowers:
        print(f"{search_flower} is in the list.")
    else:
        print(f"{search_flower} is not in the list.")
    
    # Access specific flower by its number
    try:
        index_to_access = int(input("\nEnter the number of the flower you want to access: "))
        print(f"You selected: {flowers[index_to_access - 1]}")
    except ValueError:
        print("Invalid input! Please enter a number.")
    except IndexError:
        print("That number is out of range. Please choose a number from the list.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call main function
if __name__ == "__main__":
    main()