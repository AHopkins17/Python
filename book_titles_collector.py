def main():
    # Setting up list to collect book titles
    book_titles = []

    # Collecting book titles using a while loop
    while len(book_titles) < 10:
        
        title = input("Enter a book title: ")
        # Capitalization
        book_titles.append(title.title())

    # Sorted List
    sorted_titles = sorted(book_titles)

    # Titles List 
    print("\nHere are you book titles in alphabetical order:")

    for title in sorted_titles:
        print(title)
        
# Test Program
if __name__== "__main__":
    main()