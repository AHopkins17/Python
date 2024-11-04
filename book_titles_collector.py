def main():
    
    book_titles = []

    while len(book_titles) < 10:
        
        title = input("Enter a book title: ")
        
        book_titles.append(title.title())

    sorted_titles = sorted(book_titles)

    print("\nHere are you book titles in alphabetical order:")

    for title in sorted_titles:
        print(title)
if __name__== "__main__":
    main()