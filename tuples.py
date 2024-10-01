# Create and Use Tuples

def main():
    # Create a tuple
    programming_classes = (
        'Intro to Python',
        'Advanced Python',
        'Database Essentials',
        'Web Development Basics',
        'Data Structures in Python',
        'Web Design Fundamentals'
    )

    # Header
    print("Programming Classes:")

    # Use a for loop for each class in the tuple
    for class_name in programming_classes:
        print(f"- {class_name}")

    # Calculate total number of classes in the tuple using len
    total_classes = len(programming_classes)

    # Print total number of classes
    print(f"\nTotal number of classes: {total_classes}")

# Run main function
if __name__ == "__main__":
    main()
