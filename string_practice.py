def main():
    # Example string
    example_string = "Hello, Python programmers!"

    # TODO: Iterate through the string and print each character
    print("Iterating through the string:")
    for char in example_string:
        print(char)

    # TODO: Find and print the character with the minimum ASCII value in the string
    min_char = min(example_string)
    min_ascii = ord(min_char) 
    print(f"\nCharacter with the minimum ASCII value: '{min_char}' (ASCII: {min_ascii})")

    # TODO: Find and print the character with the maximum ASCII value in the string
    max_char = max(example_string)
    max_ascii = ord(max_char)
    print(f"\nCharacter with the maximum ASCII value: '{max_char}' (ASCII: {max_ascii})")

    # TODO: Find and print the index of the first occurrence of 'o' in the string
    index_of_o = example_string.index('o')
    print(f"\nIndex of 'o': {index_of_o}")

    # TODO: Convert the string into a list of characters and print the list
    char_list = list(example_string)
    print(f"\nConverting string to a list of characters: {char_list}" )

    # TODO: Count and print the number of occurrences of 'o' in the string
    count_of_o = example_string.count('o')
    print(f"\nCount of 'o' in the string: {count_of_o}")

if __name__ == "__main__":
    main()
